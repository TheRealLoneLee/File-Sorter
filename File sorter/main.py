import os
import shutil

from time import sleep


def main():



    path = 'C:\\Users\\anicc\\Downloads'

    list_ = os.listdir(path) 

    for file_ in list_:  
        name, ext = os.path.splitext(file_)
        
        ext = ext[1:]

        if ext == '':
            continue
        
        if os.path.exists(path+'/'+ext): 
            shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
        
        else:  
            os.makedirs(path+'/'+ext) 
            shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)



while True:
    main()
    sleep(300)