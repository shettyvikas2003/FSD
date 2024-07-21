from django.db import models

# Create your models here.
class meeting(models.Model):
    meeting_code=models.CharField(max_length=30)
    meeting_dt=models.DateField(auto_now_add=True)
    meeting_subject=models.CharField(max_length=100)
    meeting_np=models.IntegerField()
