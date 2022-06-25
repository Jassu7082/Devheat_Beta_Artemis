from django.contrib import admin
from .models import ExamQp, college,students
# Register your models here.
admin.site.register(college)
admin.site.register(students)
admin.site.register(ExamQp)