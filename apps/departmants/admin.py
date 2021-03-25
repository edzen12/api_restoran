from django.contrib import admin
from apps.departmants.models import (
    Department,
    Booking,
    PhoneNumber,
)


class PhoneNumberAdmin(admin.TabularInline):
    model = PhoneNumber
    extra = 0


class DepartmentAdmin(admin.ModelAdmin):
    inlines = [PhoneNumberAdmin]


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Booking)
admin.site.register(PhoneNumber)
