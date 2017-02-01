from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from .models import *
from django.core.urlresolvers import reverse
import datetime

# Create your tests here.

class ExceptionTest(TestCase):
    #these are the relevant tests that we need to check

