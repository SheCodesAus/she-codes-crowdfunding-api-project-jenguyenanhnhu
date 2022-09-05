from rest_framework import serializers
from .models import Project, Pledge, Post, PLEDGE_TYPES, PROGRESS_TRACKER
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

class PostSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=300)
    image = serializers.FileField(required=False)
    is_technology = serializers.BooleanField()
    is_sustainability = serializers.BooleanField()
    is_education = serializers.BooleanField()
    is_diversity = serializers.BooleanField()
    is_health = serializers.BooleanField()
    is_human_rights = serializers.BooleanField()
    is_other = serializers.BooleanField()
    message = serializers.CharField(max_length=None)
    progress = serializers.ChoiceField(choices=PROGRESS_TRACKER)
    date_created = serializers.DateTimeField(read_only=True, default=timezone.now)
    next_update = serializers.DateField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image',instance.image)
        instance.message = validated_data.get('message', instance.message)
        instance.progress = validated_data.get('progress', instance.progress)
        instance.date_created = instance.date_created
        instance.next_update = validated_data.get('next_update', instance.next_update)
        instance.save()
        return instance
class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    image = serializers.URLField(required=False)
    description = serializers.CharField(max_length=None)
    goal = serializers.CharField(max_length=None)
    progress = serializers.ChoiceField(choices=PROGRESS_TRACKER)
    date_created = serializers.DateTimeField(read_only=True, default=timezone.now)
    owner = serializers.ReadOnlyField(source='owner.id')

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    updates = PostSerializer(many=True, read_only=True)

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
