from django.contrib import admin
from WebApp.models import Customer,Book,Student
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display=['name','age','address','image']

class BookAdmin(admin.ModelAdmin):
    list_display=['name','author','price','category']

class StudentAdmin(admin.ModelAdmin):
    list_display=['classroom','branch','roll_no','phone','image']




admin.site.register(Customer,CustomerAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Student,StudentAdmin)
