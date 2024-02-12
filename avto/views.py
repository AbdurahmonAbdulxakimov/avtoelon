from django.shortcuts import render
from django.db.models import Sum, F

from rest_framework import routers, serializers, viewsets, generics

from avto.models import Post, Region
from avto.serializers import (
    PostSerializer,
    RegionAvtoCountSerializer,
    PostRetriveSerializer,
)


# Create your views here.
class MainPostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().order_by("-published_at")
    serializer_class = PostSerializer
    filterset_fields = ("subcategory__category",)


class RegionAvtoCountAPIView(generics.ListAPIView):
    queryset = (
        Region.objects.all()
        .values("title")
        .filter(districts__posts__subcategory__category__title="avto")
        .annotate(region=F("title"), count=Sum("districts__posts"))
    )
    serializer_class = RegionAvtoCountSerializer


class PostRetrieveAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetriveSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().order_by("-published_at")
    serializer_class = PostSerializer
    filterset_fields = ("subcategory__category", "district__region", "json.model")

    def get_queryset(self):

        return super().get_queryset()
