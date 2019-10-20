from django.db import models

# Create your models here.
class EmployeeInfoData(models.Model):

    name = models.CharField(
        unique=True,
        max_length=100,)

    email = models.EmailField(
        max_length=100,
        blank=True,)

    phonenumber = models.CharField(
        max_length=100,
        blank=True,)

    age = models.CharField(
        max_length=100,
        blank=True,)

    class Meta:
        app_label = 'myapp'
        verbose_name = "Employee Info"

    def __str__(self):
        return self.name