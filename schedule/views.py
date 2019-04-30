import random
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, TemplateView, FormView
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
import operator
from django.contrib.auth.models import User
from django.shortcuts import render
from .filters import ClassFilter
from .models import *


class Home(TemplateView):
    template_name = 'home.html'

class ScheduleView(generic.ListView):
    model = class_schedule
    template_name = 'schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class ScheduleListView(ListView):
    model = class_schedule
    
    def get_queryset(self):
        queryset = super(ScheduleListView, self).get_queryset()
        return queryset.filter()

def search(request):
    class_list = class_schedule.objects.all()
    class_filter = ClassFilter(request.GET, queryset=class_list)
    return render(request, 'search.html', {'filter': class_filter})