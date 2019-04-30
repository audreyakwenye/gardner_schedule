from django.contrib import admin
from .models import *


class class_scheduleAdmin(admin.ModelAdmin):
    list_filter = ('classgroup', 'teacher',)
    search_fields = ('subject', 'period',)


admin.site.register(class_schedule, class_scheduleAdmin)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Period)
admin.site.register(ClassGroup)