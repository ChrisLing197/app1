import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app1.settings")
import django
django.setup()

from system import models

uname = input("Enter admin username: ")
admin = models.User(username=uname)
pswd  = input("Enter admin password: ")
admin.set_password(pswd)
admin.save()

admin_reg = models.Registration(user=admin)
admin_reg.role = models.Registration.ADMIN
admin_reg.save()
