from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, blank=True, null=True)


class Base(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        

class Advisor(Base):
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    image_url = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Photo URL'))

    def __str__(self):
        return f"{self.name}"


class BookCall(Base):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE, blank=True, null=True)
    booking_date = models.DateTimeField(null=False, blank=False, verbose_name=_("Booking DateTime"))
    
    def __str__(self):
        return f"{self.user}"