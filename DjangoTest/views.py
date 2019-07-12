from django.shortcuts import HttpResponse
from DjangoTest.Util import Tranlator, AudioSpliter
from Test import  settings
import os

BASE_DIR = settings.BASE_DIR
# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

def Split(request):
    if request.FILES:
        myFile = request.FILES.get("file")
        dir = os.path.join(os.path.join(BASE_DIR, 'static'), 'profiles')
        filePath = os.path.join(dir,myFile.name)
        destination = open(filePath, 'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
        len = AudioSpliter.spliter(filePath)
        if len==-1:
            return HttpResponse("Wrong file type.")
        chunksPath = os.path.join(dir,"chunks")
        Tranlator.translate(chunksPath, len, "wav")
        return HttpResponse("received")
    return HttpResponse("Wrong Request type")

