import numpy as np
import pandas as pd
import os
import glob

from scipy.stats import halfnorm
folders = next(os.walk('.'))[1]


for folder in folders:
    files = glob.glob(folder + "/*")
    print(files)
    for F in files:
        if ".npy" in F:
            data = np.load(F)
            print("Successfully loaded ", F)
            print(data.shape)

            noise = abs(np.random.normal(0.1,0.5,(data.shape)))
            data = data + noise

            np.save(F,data)
            print("Saved and overwritten file ",F)
            
        if ".csv" in F:
            data = pd.read_csv(F, delimiter=";",decimal=",")
            print("Successfully loaded ", F)
            
            numerics =['Delivery','Return','BackProduction']
            data[numerics] = data[numerics].astype('float')
            
            
            for col in numerics:
                nonna = (data[col] != np.nan)
                noise = abs(np.random.normal(0.1,0.5,(len(data[nonna])) ))
                data[nonna][col] += noise

            
            data[['Timestamp','Delivery','Return','BackProduction']].to_csv(F,index=False,sep=';', decimal=',')
            print("Saved and overwritten file ",F)
            
                
            
