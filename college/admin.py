from django.contrib import admin
from .models import ExamQp, college,students, result
# Register your models here.
admin.site.register(college)
admin.site.register(students)
admin.site.register(ExamQp)
admin.site.register(result)