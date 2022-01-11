from django.db import models

# Create your models here.
class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    car_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    start_time = models.DateTimeField(auto_now_add=True) #driverning ish boshlagan vaqti

    def __str__(self):
        return f"{self.first_name} {self.last_name}  -  {self.car_number}"