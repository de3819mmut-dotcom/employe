from django.contrib import admin

from .models import Department

# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('nameDepartment', 'shortNameDepartment',
                    'activeDepartment')
    search_fields = ('nameDepartment',)
    list_filter = ('nameDepartment',)

    def fullname(self, obj):
        return obj.nameDepartment


admin.site.register(Department, DepartmentAdmin)
