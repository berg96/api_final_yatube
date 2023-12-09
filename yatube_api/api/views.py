from rest_framework import viewsets

from .permissions import AuthorOrReadOnly
from .serializers import PostSerializer
from posts.models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
