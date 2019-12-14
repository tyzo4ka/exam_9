from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models import Comments, Like
from rest_framework.viewsets import ModelViewSet
from api.serializers import CommentsSerializer, LikeSerializer
from rest_framework.permissions import DjangoModelPermissions, AllowAny, DjangoModelPermissionsOrAnonReadOnly


class CommentsViewSet(viewsets.ModelViewSet):
    # authentication_classes = SessionAuthentication
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer




# class IssueViewSet(viewsets.ModelViewSet):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     queryset = Issue.objects.all()
#     serializer_class = IssueSerializer


class CommentsView(APIView):
    def post(self, request):
        comment = request.data.get("comments")
        serializer = CommentsSerializer(data=comment)
        author = request.user
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save(comments_author=author)
            return Response({"success": "Comment '{}' created successfully".format(comment_saved.text)})

    def delete(self, request, pk):
        comment = get_object_or_404(Comments.objects.all(), pk=pk)
        comment.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return Like.objects.all()
    #     return Quote.objects.filter(status=QUOTE_APPROVED)

    # def get_permissions(self):
    #     if self.action not in ['update', 'partial_update', 'destroy']:
    #         return [AllowAny()]
    #     return [IsAuthenticated()]

    # @action(methods=['post'], detail=True)
    # def like_up_or_down(self, request, pk=None):
    #     like = self.get_object()
    #     author = request.user
    #     photography = get_object_or_404()
    #     if like.like == False:
    #         photography = get_object_or_404()
    #         quote.rating += 1
    #     quote.save()
    #     return Response({'id': quote.pk, 'rating': quote.rating})
    #
    # @action(methods=['post'], detail=True)
    # def rate_down(self, request, pk=None):
    #     quote = self.get_object()
    #     quote.rating -= 1
    #     quote.save()
    #     return Response({'id': quote.pk, 'rating': quote.rating})


