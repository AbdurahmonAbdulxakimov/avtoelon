from rest_framework import serializers
from avto.models import Post
from option.serializers import PostOptionSerializer


class PostSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField(source="json.district")
    title = serializers.StringRelatedField(source="json.title", read_only=True)
    extended_title = serializers.StringRelatedField(
        source="json.extended_title", read_only=True
    )
    photo_count = serializers.IntegerField(source="json.photos_count", read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "extended_title",
            "photo_count",
            "main_photo",
            "district",
        )


class RegionAvtoCountSerializer(serializers.Serializer):
    region = serializers.CharField(max_length=256)
    count = serializers.IntegerField()


class PostRetriveSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField(source="json.district")
    title = serializers.StringRelatedField(source="json.title", read_only=True)
    options = serializers.ListField(source="json.options", read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "district", "main_photo", "photos", "price", "options")
