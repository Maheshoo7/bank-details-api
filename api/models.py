from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=256)  # branch 
    ifsc = models.CharField(max_length=500, unique=True)
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=500)
    district = models.CharField(max_length=500)
    state = models.CharField(max_length=500)

    class Meta:
        ordering = ['name']

class Bank(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return "{}".format(self.name)