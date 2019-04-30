from django.db import models
from django.utils.translation import ugettext_lazy as _

class Teacher(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Period(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class ClassGroup(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class class_schedule(models.Model):
    class_id = models.CharField(max_length=25)
    classgroup = models.ForeignKey(
        ClassGroup, null=True, blank=True,
        verbose_name=_("Classgroup"), on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        Teacher, null=True, blank=True,
        verbose_name=_("Teacher"), on_delete=models.CASCADE)

    subject = models.ForeignKey(
        Subject, null=True, blank=True,
        verbose_name=_("Subject"), on_delete=models.CASCADE)

    period = models.ForeignKey(
        Period, null=True, blank=True,
        verbose_name=_("Period"), on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ("teacher", "period",)
                

    def __str__(self):
        return self.classgroup.name + ' | ' + self.period.name + ' | ' + self.teacher.name + ' | ' + self.subject.name