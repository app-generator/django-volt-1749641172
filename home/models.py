# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    google_account = models.TextField(max_length=255, null=True, blank=True)
    nip = models.TextField(max_length=255, null=True, blank=True)
    alamat = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Asn(models.Model):

    #__Asn_FIELDS__
    nip = models.TextField(max_length=255, null=True, blank=True)
    nama = models.TextField(max_length=255, null=True, blank=True)
    asn_id = models.TextField(max_length=255, null=True, blank=True)
    alamat = models.TextField(max_length=255, null=True, blank=True)
    no_hp = models.TextField(max_length=255, null=True, blank=True)
    jabatan_id = models.ForeignKey(jabatan, on_delete=models.CASCADE)

    #__Asn_FIELDS__END

    class Meta:
        verbose_name        = _("Asn")
        verbose_name_plural = _("Asn")


class Jabatan(models.Model):

    #__Jabatan_FIELDS__
    jenis = models.TextField(max_length=255, null=True, blank=True)
    nama = models.TextField(max_length=255, null=True, blank=True)

    #__Jabatan_FIELDS__END

    class Meta:
        verbose_name        = _("Jabatan")
        verbose_name_plural = _("Jabatan")



#__MODELS__END
