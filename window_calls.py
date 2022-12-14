# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 17:09:54 2022

@author: Giles
"""

import pickle
import lzma
import numpy as np
import glob
import os

if __name__ == "__main__":
    iden = "call_ts*.xz"
    files = glob.glob(iden)
    windowed_calls = {}
    for file in files:
        with lzma.open(file,"rb") as f:
            calls = pickle.load(f)
        for i in range(12):
            up_ts = (i+1)*60*60*1000
            lw_ts = i*60*60*1000
            windowed_calls[i] = calls[np.where((calls[:,0]>lw_ts) & (calls[:,0]<up_ts))[0],:]
        
    with lzma.open("windowed_calls","wb") as f:
        pickle.dump(windowed_calls,f)
        