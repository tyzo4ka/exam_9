from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models import Comments, Like, Photography
from rest_framework.viewsets import ModelViewSet
from api.serializers import CommentsSerializer, LikeSerializer
from rest_framework.permissions import DjangoModelPermissions, AllowAny, DjangoModelPermissionsOrAnonReadOnly, \
    IsAuthenticated, BasePermission



class CommentsViewSet(viewsets.ModelViewSet):
    # authentication_classes = SessionAuthentication
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def get_permissions(self):
        if self.action not in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [DjangoModelPermissions()]




# class IssueViewSet(viewsets.ModelViewSet):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     queryset = Issue.objects.all()
#     serializer_class = IssueSerializer



class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_permissions(self):
        if self.action not in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [DjangoModelPermissions()]

    @action(methods=['post'], detail=True)
    def like_up_or_down(self, request, pk=None):
        like = self.get_object()
        author = request.user.pk
        photo = Photography.objects.get(pk=pk)
        if not like.like:
            photo.rating += 1
        else:
            photo.rating -= 1
        photo.save()
        return Response({'id': photo.pk, 'rating': photo.rating})




