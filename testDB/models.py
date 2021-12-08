from django.db import models

class emp(models.Model):
    name=models.CharField(max_length=100)
    emailID= models.CharField(max_length=100)
    country= models.CharField(max_length=100)

    class Meta:
        db_table="emp"