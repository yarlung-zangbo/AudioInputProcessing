from django.db import models

# Create your models here.
from mongoengine import *
class sound(Document):
    _id = StringField()
    name = StringField()
    content = BinaryField()
    _class = StringField()

class AudioBookV(Document):
    bookid = IntField()
    content = BinaryField()

class TestClass(Document):
    TestNumber = IntField()