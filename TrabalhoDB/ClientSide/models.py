from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    national_id = models.CharField(max_length=20)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.first_name + ' ' +self.last_name

class Address1(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='addresses1')
    address_line_1 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.client.first_name + ' ' + self.client.last_name
    

