from django.contrib import admin

from .models import Department

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
  list_display = ('name','short_name','active')
  search_fields = ('name',)
  list_filter = ('name',)
  def fullname(self, obj):
    return obj.name
  
admin.site.register(Department, DepartmentAdmin)
