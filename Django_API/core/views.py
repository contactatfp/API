from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'Kyle',
            'age': 30
        }
        return Response(data)


# Create your views here.
def test_view(request):
    data = {
        'name': 'Kyle',
        'age': 30
    }
    return JsonResponse(data)
