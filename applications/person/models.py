from django.db import models

# Create your models here.
class Person(models.Model):
  name = models.CharField('name', max_length=50, editable=False)
  lastname = models.CharField('lastName', max_length=50, editable=False)
  job = models.CharField('job', max_length=1, choices=JOB_CHOICES)
  class Meta:
    verbose_name = 'Person'
    verbose_name_plural = 'Persons'
    ordering = ['name']
    unique_together = ('name', 'lastname')
  def __str__(self):
    return self.name + '-' + self.lastname