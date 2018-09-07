import os
import numpy as np
from numpy import random,mat
import pandas as pd
datestring = '20180602'
wavelength = '405nm'
#pwd = os.getcwd()#获取当前目录，C：表示当前目录，用法同Matlab pwd 
pwd = os.path.dirname(os.getcwd())    
DateFolderPath = os.path.join(pwd,'原始数据',wavelength,datestring)
DateFolder = os.listdir(DateFolderPath)
n = 1
x = DateFolder[0]
for i in range(0,len(DateFolder)):#样品的名称
    path = os.path.join(DateFolderPath,DateFolder[i])
    if os.path.isdir(path):
        DataFolder = os.listdir(path)
        for j in range(0,len(DataFolder)):#样品的具体浓度
            print(DataFolder[j])
            DataPath = os.path.join(path,DataFolder[j])
            if os.path.isdir(DataPath):  
                DataFiles = os.listdir(DataPath)
                AllData1 =[]
                AllData = []
                for k in range(0,len(DataFiles)):#存放60条光谱数据
                    DataFilesPath = os.path.join(DataPath,DataFiles[k])
                    f = open(DataFilesPath)
                    Data = []
                    for line in f.readlines()[14:len(f.readlines())-1]:
                        p_tmp, E_tmp = [float(m) for m in line.split()] 
                        Data.append(E_tmp)
                    AllData1 = mat(Data) 
                    if AllData == []:
                        AllData = AllData1
                    else:
                        AllData = np.vstack((AllData,AllData1))  
            print(pwd)            
            savepath =  os.path.join(pwd,'pyFinishedTxt',wavelength,datestring) 
            isExist = os.path.exists(savepath) 
            if not isExist:
                os.makedirs(savepath)
                print(savepath+'创建成功')
            else:
                print(savepath+'目录存在')
            np.savetxt(os.path.join(savepath,DataFolder[j]+'.txt'),AllData)   
            print('ddd') 
                    
                        
                    
                    #print(lines)
                    #for line in f.readlines()[15:17]:
                        
                    
                    #data = pd.read_csv(DataFilesPath)
                    #print(data)