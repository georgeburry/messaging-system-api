from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .handlers import create_message
from .models import Message
from .serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Message.objects.filter(users=user).order_by('timestamp')

        # Filter by user if user_id is provided in the query params
        user_id = self.request.query_params.get('user_id', None)
        if user_id:
            queryset = queryset.filter(users__id=user_id)

        return queryset

    def list(self, request, *args, **kwargs):
        raise PermissionDenied("Listing messages is not allowed.")

    def retrieve(self, request, *args, **kwargs):
        raise PermissionDenied("Retrieving a message is not allowed.")

    @action(detail=False, methods=['post'], url_path='create')
    def create_message(self, request):
        content = request.data.get('content')
        author = self.request.user
        user_ids = request.data.get('user_ids', [])
        if not content or not user_ids:
            return Response({'detail': 'Content and user_ids are required.'}, status=status.HTTP_400_BAD_REQUEST)
        message = create_message(content=content, author=author, user_ids=user_ids)
        return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_path='retrieve')
    def retrieve_messages(self, request):
        messages = self.get_queryset()
        return Response(MessageSerializer(messages, many=True).data)

    @action(detail=False, methods=['get'], url_path='search')
    def search_messages(self, request):
        keyword = request.query_params.get('keyword')
        if not keyword:
            return Response({'detail': 'Keyword is required.'}, status=status.HTTP_400_BAD_REQUEST)

        messages = self.get_queryset().filter(content__icontains=keyword)
        return Response(MessageSerializer(messages, many=True).data)
