from django.db import models

# Create your models here.
from mongoengine import *
class sound(Document):
    _id = StringField()
    name = StringField()
    content = BinaryField()
    _class = StringField()