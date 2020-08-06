from django.db import models


class Student(models.Model):
	name = models.CharField(max_length=20, )
	course = models.CharField(max_length=20, )
	college = models.CharField(max_length=30, )
	fees = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.name
