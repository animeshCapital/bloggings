from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

def profile_image(obj, filename):
    paths = "profile_image/%s/%s"%(obj.user.username,filename)
    return paths

class UserProfile(models.Model):
    image = models.ImageField(upload_to='profile_image' ,null=True, blank=True)
    phone_no = models.CharField(max_length=15, null=True)
    user = models.OneToOneField(User, on_delete=True)
 

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(UserProfile, self).delete(*args, **kwargs)
        storage.delete(path)

@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()