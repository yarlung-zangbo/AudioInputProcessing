import ffmpeg
import os
from pydub import *
def concat(file1,file2,output):
    Stream1 = AudioSegment.from_file(file1)
    Stream2 = AudioSegment.from_file(file2)
    Stream3 = Stream1+Stream2
    Stream3.export(output,format = "wav")

def tickformat(file,audiotype):
    save_name = os.path.splitext(file)[0]+'.'+audiotype
    try:
        out,err = (
            ffmpeg.input(file)
            .output(save_name)
            .overwrite_output()
            .run()
        )
        return save_name
    except Exception as e:
        print(e)

