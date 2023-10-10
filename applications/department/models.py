from django.db import models

# Create your models here.


class Department(models.Model):
    nameDepartment = models.CharField('nameDepartment', max_length=50)
    shortNameDepartment = models.CharField(
        'shortNameDepartment', max_length=2, unique=True)
    activeDepartment = models.BooleanField('active', default=False)
    search_fields = ('nameDepartment', 'shortNameDepartment',)
    list_filter = ('nameDepartment',)

    class Meta:
        verbose_name = 'nameDepartment'
        verbose_name_plural = 'nameDepartments'
        ordering = ['nameDepartment']
        unique_together = ('nameDepartment', 'shortNameDepartment')

    def __str__(self):
        return self.nameDepartment + ' - ' + self.shortNameDepartment
