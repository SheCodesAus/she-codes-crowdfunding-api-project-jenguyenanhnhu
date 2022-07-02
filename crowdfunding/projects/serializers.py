from rest_framework import serializers
from .models import Project, Pledge, PLEDGE_TYPES, CATEGORIES, SKILLS

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    type = serializers.ChoiceField(choices=PLEDGE_TYPES)
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    hours = serializers.DecimalField(max_digits=12, decimal_places=2)
    skill_set = serializers.MultipleChoiceField(choices=SKILLS)
    name = serializers.CharField(max_length=100)
    email_address = serializers.EmailField()
    resources = serializers.CharField(max_length=None)
    comment = serializers.CharField(max_length=300)
    anonymous = serializers.BooleanField()
    supporter = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()
    
    # if type=='$':
    #     class PledgeMoney(models.Model):
    #         amount = models.DecimalField(max_digits=12, decimal_places=2)
    #         # more code for processing payment
    # if type=='T':
    #     class PledgeTime(models.Model):
            
    # if type=='A':
    #     class PledgeAdvice(models.Model):
    #         name = models.CharField(max_length=100)
    #         email_address = models.CharField(max_length=100)
    # if type=='R':
    #     class PledgeResources(model.Model):
    #         resources = models.TextField()
    #         name = models.CharField(max_length=100)
    #         email_address = models.CharField(max_length=100)
    # comment = models.CharField(max_length=200)
    # supporter = models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE,
    #     related_name='supporter_pledges'
    # )
    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    image = serializers.FileField(required=False)
    description = serializers.CharField(max_length=None)
    categories = serializers.MultipleChoiceField(required=False, choices=CATEGORIES)
    goal = serializers.CharField(max_length=None)
    seeking = serializers.MultipleChoiceField(choices=PLEDGE_TYPES)
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
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
