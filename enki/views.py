from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Form, FormRecordAttributeType, FormRecordReference, Project

class IndexView(generic.ListView):
    template_name = 'enki/index.html'
    context_object_name = 'all_projects_list'

    def get_queryset(self):
        """Return the last five published questions.(Not including those set to be published in the future)"""
        return Project.objects.filter(date_created__lte=timezone.now()).order_by('-date_created')[:5]
        return Project.objects.order_by('-date_created')[:5]