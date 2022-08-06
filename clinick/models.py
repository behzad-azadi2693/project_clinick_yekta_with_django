from tabnanny import verbose
from django.db import models
from django.core.validators import RegexValidator
from django.contrib import admin

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url = models.URLField(verbose_name='آدرس لینک')
    image = models.ImageField(upload_to='slider/',verbose_name='تصویر' )
    status = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر'

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Slider, self).delete()

    def save(self, *args, **kwargs):
        try:
        
            this = Slider.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except: 
            pass

        super(Slider, self).save(*args, **kwargs)


class CustomerInfo(models.Model):
    name = models.CharField(max_length=150,verbose_name='نام')
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 13,verbose_name='شماره تلفن')
    address = models.TextField(verbose_name='آدرس')
    subject = models.CharField(max_length=150,verbose_name='حوزه مشاوره')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    class Meta:
        verbose_name = 'اطلاعات'
        verbose_name_plural = 'اطلاعات'
    
    @admin.display(description='تاریخ')
    def created(self):
        return self.created
    
    def __str__(self):
        return self.name


class SiteSetting(models.Model):
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 13,verbose_name='شماره تلفن')
    email = models.EmailField(max_length=150,verbose_name='ایمیل')
    address = models.CharField(max_length=150,verbose_name='آدرس')
    instagram = models.CharField(max_length=200,verbose_name='لینک اینستاگرام')
    subject = models.CharField(max_length=100,verbose_name='عنوان توضیحات')
    description = models.TextField(verbose_name='توضیحات')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.email
