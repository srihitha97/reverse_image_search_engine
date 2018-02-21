import os
from os.path import join
import cv2
import numpy as np
import time as time
import scipy.spatial.distance as dist
directory="C:\Users\Haribabu.SRIHITHA\Desktop\pesize"
searchImage="C:\Users\Haribabu.SRIHITHA\Desktop\pesize\CANON SHOTS 019.jpg"
index={}
def find(directory):
      for (dirname,dirs,files) in os.walk(directory):
          for filename in files:
              if (filename.endswith(".jpg")):
                  fullpath=join(dirname,filename)
                  index[fullpath]=features(fullpath)

      print "total number of photos in this directory %s"%len(index)
      return index


def features(imageDirectory):
    img = cv2.imread(imageDirectory)
    histogram = cv2.calcHist([img], [2], None,[ 256],[0, 256])
    Nhistogram = cv2.normalize(histogram,histogram)
    return Nhistogram

def search(SearchImage,SearchDir):
     histim=features(SearchImage)
     allimages=find(SearchDir)
     match=top(histim,allimages)
     return match
def top(histim,allimages):
      correlation={}
      for (address,value) in allimages.items():
        correlation[address]=cv2.compareHist(histim,value,cv2.HISTCMP_CHISQR)
      ranked=sorted(correlation.items() ,key=lambda tup:float(tup[1]))
      print ranked
      return ranked[0:5]
dir="C:\Users\Haribabu.SRIHITHA\Desktop\pesize"
sea="C:\Users\Haribabu.SRIHITHA\Desktop\pesize\CANON SHOTS 019.jpg"

finalOutput = search(sea,dir)

for imageAdd,Histvalue in finalOutput:
    image=cv2.imread(imageAdd)
    resized=cv2.resize(image,(0,0),fx=0.25,fy=0.25)
    cv2.imshow("image directory %s %s"% (imageAdd,Histvalue),resized)
    cv2.waitKey(1000)
