from django import forms
from .models import CustomerInfo

messages = {
    'required':'این فیلد الزامی است',
    'invalid':'این فیلد صحیح نمیباشد',
    'max_length':'اندازه فیلد بیشتر از حد مجاز',
    'min_length':'اندازه فیلد کمتر از حد مجاز',
}

class CustomerInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerInfoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
            self.fields['name'].widget.attrs['placeholder'] = 'نام و نام خانوادگی'
            self.fields['phone'].widget.attrs['placeholder'] = 'شماره تلفن'
            self.fields['subject'].widget.attrs['placeholder'] = 'حوزه مشاوره'
            self.fields['address'].widget.attrs['placeholder'] = 'آدرس'
            self.fields[field].error_messages = messages

    class Meta:
        model = CustomerInfo
        fields = '__all__'