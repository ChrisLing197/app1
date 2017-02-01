from django.db.models.signals import post_save
from . import models

def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        profile = models.Registration(user=user)
        profile.save()

#post_save.connect(create_profile, sender=models.User, dispatch_uid="users-profilecreation-signal")
