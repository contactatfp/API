from django.shortcuts import render
from django.http import JsonResponse

# 3rd party imports
from rest_framework import mixins, generics, status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# from rest_framework.views import APIView
# from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post


# POST VIEW CLASS DOES NOT REQUIRE AUTHENTICATION
class PostView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# THE AUTHENTICATED VIEWS REQUIRE AUTHENTICATION FOR GET ALL CREATE NEW POST
class AuthenticatedViews(ListAPIView, mixins.CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class TestView(APIView):
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
#
#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         # return one post
#         # post = qs.first()
#         # serializer = PostSerializer(post)
#         # return all posts
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
