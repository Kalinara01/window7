from .serializers import CommentSerializer, RatingSerializer
from .models import Comment, Rating
from rest_framework.viewsets import ModelViewSet


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
