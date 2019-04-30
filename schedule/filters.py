import django_filters
from .models import *

class ClassFilter(django_filters.FilterSet):
    class Meta:
        model = class_schedule
        fields = ['classgroup', 'teacher', 'subject', 'period']