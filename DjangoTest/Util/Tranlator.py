from aip import AipSpeech
import os
import jieba
from DjangoTest.Util.AudioUtil import *
from DjangoTest.DAO import soundDAO

APP_ID = "16682530"
API_KEY = "AHo1rGgmZy29ULcCPyBVxcrY"
SECRET_KEY = "rtwOSBH7kEjoVrghtfW52MNsWqLupi9Z"

client = AipSpeech(APP_ID, API_KEY,SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
def translate(dirPath,len,audioType):
    textFile = os.path.join(dirPath,"text.txt")
    soundEffectPath = os.path.join(dirPath,"effect.mp3")
    file = open(textFile,"w+")
    for i in range(len):
        audioname = '%04d.%s'%(i,audioType)
        audioPath = os.path.join(dirPath,audioname)
        res = client.asr(get_file_content(audioPath), audioType, 16000, {
            'dev_pid': 1537,
        })
        line = res.get("result")[0]
        seg_list = jieba.cut(line,cut_all=False)
        print(seg_list)
        j=0
        SEInputFileName = audioname
        for word in seg_list:
            print(word)
            soundEffect = soundDAO.find(word)
            if soundEffect:
                SEF = open(soundEffectPath,"wb+")
                SEF.write(soundEffect[0].content)
                SETPath = tickformat(soundEffectPath,"wav")
                SEF.close()
                os.remove(soundEffectPath)
                print(SEInputFileName,audioname)
                SEInputPath = os.path.join(dirPath,SEInputFileName)
                outFileName = '%04d%s.%s'%(j,'_SE',audioType)
                print(SEInputFileName,audioname)
                print("Input1: %s, Input2: %s" % (SEInputPath,SETPath))
                SEOutPath = os.path.join(dirPath,outFileName)
                concat(SEInputPath,SETPath,SEOutPath)
                j = j + 1
                SEInputFileName = outFileName
        print(res)
        file.write(line)

