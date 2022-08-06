from django.contrib import admin
from .models import Slider, CustomerInfo, SiteSetting
# Register your models here.
from django.core.exceptions import PermissionDenied
from jalali_date import datetime2jalali, date2jalali

@admin.register(CustomerInfo)
class CustomerInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','تاریخ')
    list_display_links = ('id', 'name')

    def تاریخ(self, obj):
        return datetime2jalali(obj.created).strftime('%Y/%m/%d _ %H:%M:%S')


def delete_selected(modeladmin, request, queryset):
    if not modeladmin.has_delete_permission(request):
        raise PermissionDenied
    if request.POST.get('post'):
        pass
        queryset.update(status=False)
    else:
        return delete_selected(modeladmin, request, queryset)
    return False

@admin.register(Slider)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','تاریخ')
    list_display_links = ('id', 'title')

    actions = [delete_selected]

    def تاریخ(self, obj):
        return datetime2jalali(obj.created).strftime('%Y/%m/%d _ %H:%M:%S')

delete_selected.short_description = "غیرفعال کردن"

@admin.register(SiteSetting)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('id','phone','email','تاریخ')
    actions = [delete_selected]

    def تاریخ(self, obj):
        return datetime2jalali(obj.created).strftime('%Y/%m/%d _ %H:%M:%S')