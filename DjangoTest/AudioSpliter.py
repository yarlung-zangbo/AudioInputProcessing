#coding=utf-8
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import sys

# 初始化
def spliter():
    audiopath = "D:\SEI\week19\Test\DjangoTest\zoo.mp3"
    audiotype = 'mp3' #如果wav、mp4其他格式参看pydub.AudioSegment的API
    # 读入音频
    print('读入音频')
    sound = AudioSegment.from_file(audiopath, format=audiotype)
    sound = sound[:3*60*1000] #如果文件较大，先取前3分钟测试，根据测试结果，调整参数
    # 分割
    print('开始分割')
    chunks = split_on_silence(sound,min_silence_len=300,silence_thresh=-70)#min_silence_len: 拆分语句时，静默满0.3秒则拆分。silence_thresh：小于-70dBFS以下的为静默。
    print(chunks)
    # 创建保存目录
    filepath = os.path.split(audiopath)[0]
    print(os.path.split(audiopath))
    chunks_path = filepath+'/chunks/'
    if not os.path.exists(chunks_path):os.mkdir(chunks_path)
    # 保存所有分段
    print('开始保存')
    for i in range(len(chunks)):
        new = chunks[i]
        save_name = chunks_path+'%04d.%s'%(i,audiotype)
        new.export(save_name, format=audiotype)
        print('%04d'%i,len(new))
    print('保存完毕')
spliter()
