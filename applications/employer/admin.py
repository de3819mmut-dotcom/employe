from django.contrib import admin

# Register your models here.
from .models import Employer, Skills
# Register your models here.


class EmployerAdmin(admin.ModelAdmin):
  list_display = ('name', 'lastname', 'job', 'department','fullname')
  search_fields = ('name',)
  list_filter = ('id','department','job','skills',)
  filter_horizontal=('skills',)
  def fullname(self, obj):
    return obj.lastname + '-' + obj.name
  
admin.site.register(Employer,EmployerAdmin)
admin.site.register(Skills)