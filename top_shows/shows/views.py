from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from shows.spider import scrape
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from shows.serializers import ShowSerializer
from shows.models import Show

@api_view(["GET"])
@csrf_exempt
def run_scrape(request):
    scrape()
    return HttpResponseRedirect(redirect_to='/api/v1/shows/')

class ListShowAPIView(ListAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer