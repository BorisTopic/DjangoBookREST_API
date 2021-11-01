from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class FictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Fiction')
    serializer_class = BookSerializer


class PhilosophyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Philosophy')
    serializer_class = BookSerializer


class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Horror')
    serializer_class = BookSerializer


class HolidayViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Holiday')
    serializer_class = BookSerializer


class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Fantasy')
    serializer_class = BookSerializer


class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Mystery')
    serializer_class = BookSerializer


class SelfHelpViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Self Help')
    serializer_class = BookSerializer


class AdventureViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Adventure')
    serializer_class = BookSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='History')
    serializer_class = BookSerializer


class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Romance')
    serializer_class = BookSerializer