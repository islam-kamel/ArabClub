from django.contrib.auth import get_user_model
from rest_framework import serializers
from tag_system.serializer import FollowTagsSerializers
from user_profile.serializer import (
    AddressSerializer,
    BioSerializer,
    GitHubSerializer,
    NameSerializer,
    PhoneSerializer,
    SkillsSerializer,
)


class UserSerializer(serializers.ModelSerializer):
    """
    Update all information for users from one end point
    this class can call all related others classes with 'other func'
    each class is responsible for updating the information about
    """

    bio = BioSerializer(required=False)
    phone = PhoneSerializer(required=False)
    skills = SkillsSerializer(required=False)
    name = NameSerializer(required=False)
    address = AddressSerializer(required=False)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    date_of_birth = serializers.DateField(required=False)
    github = GitHubSerializer(required=False)
    follow_tag = FollowTagsSerializers(required=False, many=True)

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "name",
            "username",
            "email",
            "date_of_birth",
            "bio",
            "skills",
            "github",
            "phone",
            "address",
            "follow_tag",
        ]
