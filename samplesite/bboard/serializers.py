from rest_framework import serializers
from .models import (
    Rubric,
    Profile,
    Technology,
    Education,
    Expertise,
    Bd,
)


class RubricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubric
        fields = ('id', 'pk', 'name')


class BdSerializer(serializers.ModelSerializer):
    rubric = RubricSerializer()

    class Meta:
        model = Bd
        fields = ('id', 'title', 'content', 'rubric', 'price')


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'name']


class ProfileSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True)

    class Meta:
        model = Profile
        fields = (
            'name',
            'surname',
            'salary_min',
            'email',
            'is_hired',
            'birth_date',
            'expertise',
            'education',
            'technologies',
        )


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['name']


class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = ['name']
