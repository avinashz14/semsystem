from django.db import models
from django.contrib.auth.models import User
from djanog.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, default='')
    loc = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default='')
    image = models.ImageField(upload_to='profile_image', blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs)
    instance.profile.save()