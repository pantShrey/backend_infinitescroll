from django.db.models import Prefetch, Count
from django.db.models.functions import Random
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import CursorPagination
from .models import Post, Comment
from .serializers import PostSerializer

class PostPagination(CursorPagination):
    page_size = 10
    
    def get_ordering(self, request, queryset, view):
        # Check if random ordering is requested
        if request.query_params.get('order_mode') == 'random':
            return (Random(),)
        return ('-timestamp',) 

class PostViewSet(ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        # Fetch query parameters
        comment_mode = self.request.query_params.get('comment_mode', 'latest')
        order_mode = self.request.query_params.get('order_mode', 'latest')
        
        # Determine comment ordering
        if comment_mode == 'random':
            comments_qs = Comment.objects.order_by(Random())
        else:  # Default to latest comments
            comments_qs = Comment.objects.order_by('-timestamp')

        # Prefetch comments without slicing
        comments_prefetch = Prefetch(
            'comments',
            queryset=comments_qs,
            to_attr='all_comments'
        )

        # Main post queryset
        queryset = Post.objects.select_related('user').prefetch_related(
            comments_prefetch
        ).annotate(
            comment_count=Count('comments')
        )

        # Determine post ordering
        if order_mode == 'random':
            queryset = queryset.order_by(Random())
        else:  # Default to latest posts
            queryset = queryset.order_by('-timestamp')

        return queryset





