from django.db import models

class college(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(('password'), max_length=128)
    dob = models.CharField(max_length=10)

class students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(('password'), max_length=128)
    dob = models.CharField(max_length=10)

class ExamQp(models.Model):
    examName = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='exam/pdf/')
    date = models.CharField(max_length=10)

    def __str__(self):
        return self.examName

