from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('NS', '--'))
CONTRIBUTOR_CHOICES = ( ('Y' , 'Yes') , ('N' , 'NO') , ('NS' , '--' ) )  
class CustomUser(AbstractUser):
    gender = models.CharField(max_length = 2, choices = GENDER_CHOICES, default = GENDER_CHOICES[2][0])
    profile_pic = models.ImageField(upload_to = 'profile_pics/', blank = True)
    dob = models.DateField(null = True, blank = True)
    phone_number = models.CharField(max_length = 12, unique = True, default = '')
    following = models.ManyToManyField('self', symmetrical = False, related_name = 'followers', blank = True)
    contributor = models.CharField(max_length = 2, choices = CONTRIBUTOR_CHOICES, default = CONTRIBUTOR_CHOICES[2][0])
    

    class Meta:
        unique_together = ('email',)
        verbose_name = 'User'     

    
