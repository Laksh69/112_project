import os
import shutil

source="/Users/richakapoor/Downloads"

list_of_files=os.listdir(source)
#print(list_of_files)

for fileName in list_of_files:
    name,extension=os.path.splitext(fileName)
    #print(name)
    #print(extension)
    if extension=="":
        continue
    if extension in [ ".txt", ".doc", '.docx', ".pdf"]:
        path1= source+"/"+ fileName
        path2= source+"/"+"documentFiles"
        path3=source+"/"+"documentFiles"+"/"+fileName
        #print("path1 is :",path1)
        #print("path3 is :",path3)
        if os.path.exists(path2):
            print("moving ",fileName," ...")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)    
            print("moving ",fileName," ...")
            shutil.move(path1,path3)