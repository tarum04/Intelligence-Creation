from django.db import models


# Create your models here.
STATUS_CHOICES = (
    ("SUCCESS", "Success"),
    ("FAILED", "Failed"),
    ("ON-GOING", "On-Going"),
)

class Record(models.Model):
    masalah = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    features = models.CharField(max_length=100)
    kategori = models.CharField(max_length=20)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)

    def __str__(self):
        return self.masalah
    
class RecordDetail(models.Model):
    masalahKey = models.ForeignKey(Record, on_delete=models.CASCADE)
    note = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()