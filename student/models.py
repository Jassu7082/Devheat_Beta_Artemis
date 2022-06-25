from django.db import models

class ExamUpl(models.Model):
    examCode = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='exam/updf/')

    def __str__(self):
        return self.examCode