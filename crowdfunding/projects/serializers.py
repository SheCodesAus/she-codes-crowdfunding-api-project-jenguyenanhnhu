from rest_framework import serializers
from .models import Project, Pledge, PLEDGE_TYPES, CATEGORIES, SKILLS
from django.utils import timezone

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    type = serializers.ChoiceField(choices=PLEDGE_TYPES)
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=300)
    supporter = serializers.ReadOnlyField(source='supporter.id')
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.type = instance.type
        instance.amount = instance.amount
        instance.comment = validated_data.get('comment', instance.comment)
        instance.supporter = instance.supporter
        instance.project_id = instance.project_id
        instance.save()
        return instance

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    image = serializers.FileField(required=False)
    description = serializers.CharField(max_length=None)
    goal = serializers.CharField(max_length=None)
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField(read_only=True, default=timezone.now)
    owner = serializers.ReadOnlyField(source='owner.id')

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
