from django.db import models

from utils.models import BaseModel


class Region(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class District(BaseModel):
    title = models.CharField(max_length=256)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="districts"
    )

    is_filter = models.BooleanField(default=False)

    def __str__(self):
        return self.title
