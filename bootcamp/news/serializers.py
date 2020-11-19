from rest_framework import routers, serializers, viewsets, permissions
from bootcamp.news.models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-timestamp')
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticated]