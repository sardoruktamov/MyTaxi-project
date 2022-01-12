from django.db import models
from client.models import Client
from driver.models import Driver

# Create your models here.
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  #zakas berilgan vaqt
    update_at = models.DateTimeField(auto_now=True)       #zakas o'zgartirilgan vaqt

    def __str__(self):
        return str(self.client)

class OrderStatus(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status

class AcceptOrder(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client} >> {self.driver}  -  {self.status}"


