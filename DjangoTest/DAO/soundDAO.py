from mongoengine import *
from DjangoTest.models import sound
connect("YueSheng")
def find(name):
    result = sound.objects(name = name)
    return result