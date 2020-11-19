from rest_framework import routers
from bootcamp.news.serializers import NewsViewSet

router = routers.DefaultRouter()
router.register("news", NewsViewSet)
