from django.db import models

class RegisteredUser(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    last_name = models.CharField(max_length=50)
    frist_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11, default='09100000000')
    City = models.CharField(max_length=50, default='تهران')


    def __str__(self):
        return self.user_name
