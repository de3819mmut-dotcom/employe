from django.db import models
from applications.department.models import Department
from ckeditor.fields import RichTextField
# Create your models here.
JOB_CHOICES = (
    ('0', 'Ingeniero'),
    ('1', 'Arquitecto'),
    ('2', 'Desarrollador'),
    ('3', 'Programador'),
)


class Skills(models.Model):
    skill = models.CharField('skill', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.skill + ' - ' + str(self.id)


class Employer(models.Model):
    name = models.CharField('name', max_length=50)
    lastname = models.CharField('lastName', max_length=50)
    job = models.CharField('job', max_length=1, choices=JOB_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    cv = RichTextField(default='None', blank=True)
    avatar = models.ImageField(upload_to='empleados', blank=True, null=True)
    fullname = models.CharField(
        'fullName', max_length=200, blank=True, null=True)
    skills = models.ManyToManyField(Skills)
    # image = models.ImageField('image', upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.lastname + ' - ' + self.job + ' - ' + self.name
