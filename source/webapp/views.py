from django.shortcuts import render
from django.views.generic import ListView, DetailView

from webapp.models import Photography


class IndexView(ListView):
    model = Photography
    template_name = 'index.html'
    ordering = ['-created_date']


class PhotoView(DetailView):
    template_name = "photo/detail.html"
    model = Photography

