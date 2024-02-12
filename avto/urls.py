from django.urls import path, include
from avto import views

urlpatterns = [
    path("main/", views.MainPostListAPIView.as_view()),
    path("region_avtos/", views.RegionAvtoCountAPIView.as_view()),
    path("a/show/<int:pk>/", views.PostRetrieveAPIView.as_view()),
]
