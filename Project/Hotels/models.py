from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=50)  

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)  
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities')  # Связь с регионом

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=50)  
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')  # Связь с городом

    def __str__(self):
        return self.name

