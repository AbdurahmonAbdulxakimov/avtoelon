from django.db import models
from user.models import User
from utils.models import BaseModel

from common.models import District, Region


# Create your models here.
class Category(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class SubCategory(BaseModel):
    title = models.CharField(max_length=256)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategories"
    )
    has_price = models.BooleanField(default=True)
    options = models.ManyToManyField(
        "option.Option",
    )

    def __str__(self):
        return self.title


class Post(BaseModel):
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="posts"
    )

    published_at = models.DateTimeField(auto_now_add=True)
    info = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    views = models.IntegerField(default=0, editable=False)

    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="posts"
    )

    phone = models.CharField(max_length=16)

    is_active = models.BooleanField(default=True)
    favorite_of = models.ManyToManyField(User, related_name="posts")

    def __str__(self):
        return self.info


class Photo(BaseModel):
    image = models.ImageField(upload_to="photos")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="photos")
    is_main = models.BooleanField(default=False)


class UserNotePost(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.content
