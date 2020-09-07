from django.db import models




class Account(models.Model):
	firstname=models.CharField(max_length=20)
	lastname=models.CharField(max_length=10)
	email=models.EmailField()
	number=models.CharField(max_length=10)
	address1=models.TextField()
	address_2=models.TextField(default=None)
	city = models.CharField(max_length=10)
	zipcode = models.CharField(max_length=10)
	state=models.CharField(max_length=10)

	def __str__(self):
		return (self.firstname +" "+self.lastname)
