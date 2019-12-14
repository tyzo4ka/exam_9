from django.shortcuts import render
from django.views.generic import ListView
from webapp.models import Photography


class IndexView(ListView):
    model = Photography
    template_name = 'index.html'
    ordering = ['-created_date']

    # def get_queryset(self):
    #     return Photography.objects.filter(created_date=)
