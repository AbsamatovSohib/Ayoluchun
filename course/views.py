from django.db.models.query import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView
from course.models import Course
from rest_framework.filters import SearchFilter
from course.serializer import (
    CourseSerializer,
)
from django.db import models


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ("title", "buy_user")

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                is_buy=models.Case(
                    models.When(buy_user=self.request.user, then=True),
                    default=False,
                    output_field=models.BooleanField(),
                ),
                buyers_count=models.Count("buy_user"),
            )
        )
