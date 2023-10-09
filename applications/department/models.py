from django.db import models

# Create your models here.
class Department(models.Model):
  name = models.CharField('name', max_length=50)
  short_name = models.CharField('short_name', max_length=20, blank=True, unique= True)
  active = models.BooleanField('active', default=False)
  search_fields = ('name','short_name',)  
  list_filter = ('name',)
  class Meta:
    verbose_name = 'Department'
    verbose_name_plural = 'Departments'
    ordering = ['name']
    unique_together = ('name', 'short_name')
  def __str__(self):
    return self.name + ' - ' + self.short_name