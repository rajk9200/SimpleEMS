from django.db import models

# Create your models here.


class Employee(models.Model):
    GENDER_CHOICES = (
        ('', 'Select Gender'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name=models.CharField(max_length=100)
    pan_number =models.CharField(max_length=10,unique=True)
    age =models.CharField(max_length=100)
    gender =models.CharField(choices=GENDER_CHOICES, max_length=8)
    email =models.EmailField(unique=True)
    city = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table='employee'


    def __str__(self):
        return self.name

class Cities(models.Model):
    name =models.CharField(max_length=200)

    def __str__(self):
        return self.name