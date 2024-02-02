from typing import Any
from rest_framework import serializers
from users.models import User
from course.models import Course


class CourseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "first_name", "last_name")


class CourseSerializer(serializers.ModelSerializer):
    is_buy = serializers.BooleanField()
    buy_user = CourseUserSerializer(many=True)
    by_users_count = serializers.IntegerField()

    class Meta:
        model = Course
        fields = (
            "title",
            "price",
            "image",
            "price",
            "short_content",
            "is_buy",
            "by_users_count",
            "buyers_count",
        )

    def to_representation(self, instance: Any) -> Any:
        json = super().to_representation(instance)
        json["by_users_count"] = json["by_users_count"][:5]
        return json