from django.contrib import admin
from .models import Resume
@admin.register(Resume)
# Register your models here.
class ResumeAdmin(admin.ModelAdmin):
    list_display=["id","name","dob","gender",
    'city','pin','state','mobile','job_city',
    'profile_image','my_file']
