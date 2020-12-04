import serial

import matplotlib.pyplot as plt
import random
from scipy.signal import find_peaks
import numpy as np
# 25 samples per second (in algorithm.h)
SAMPLE_FREQ = 25
# taking moving average of 4 samples when calculating HR
# in algorithm.h, "DONOT CHANGE" comment is attached
MA_SIZE = 4
# sampling frequency * 4 (in algorithm.h)
BUFFER_SIZE = 100

def smooth_curve_test(points, sample_size):
    smoothed_points = []
    reads = [0 for _ in range(sample_size)]
    id_reads = 0
    for id, point in enumerate(points):
        reads[id_reads] = point
        id_reads += 1

        if id_reads % sample_size == 0:
            id_reads = 0
            smoothed_points.append((sum(reads)/sample_size, id))

    return smoothed_points

def analisisHR():
    global hrValues
    global miliValues
    '''for i in range(0, 96):
        valores.append((hrValues[i]+hrValues[i+1]+hrValues[i+2])/3);
        valoresMili.append((miliValues[i]+miliValues[i+1]+miliValues[i+2])/3)'''
    nuevosValores1= smooth_curve_test(hrValues, 15)
    nuevosValores=[i for (i,j) in nuevosValores1 ]
    len(nuevosValores);
    peaks = find_peaks(nuevosValores)[0]
    
    plt.plot(nuevosValores);
    #print(peaks)
    plt.scatter(peaks, [nuevosValores[j] for j in peaks], marker='+', c='Red')
    #plt.show()
    #print(len(nuevosValores));
    bajada=False
    palpitacionAnterior=-1
    palpitaciones=[]
    for i in range(0, len(peaks)-1):
        palpitaciones.append(miliValues[peaks[i+1]]-miliValues[peaks[i]]);
    print(palpitaciones)
    tiempoPromedio=sum(palpitaciones)/len(palpitaciones)
    valorHR=(60000*len(peaks))/(miliValues[-1]-miliValues[0])
    print("duracion:", miliValues[-1]-miliValues[0], valorHR)


ser=serial.Serial("/dev/cu.usbmodem14201", 9600);
hrValues=[]
miliValues=[]
redValues=[]
irValues=[]

while(1):
    try:
        lineBytes=ser.readline();
        line=lineBytes.decode("ascii")
        line=line.rstrip();#HR:118;ML:1704
        print(line)
        medidas=line.split(";") #["HR:118", "ML:1704"]
        hr=int(medidas[0].split(":")[1]) #["HR", "118"], toma el 118, lo convierte a int y lo guarda
        milis=int(medidas[1].split(":")[1]) #["ML", "1704"]
        hrValues.append(hr)
        miliValues.append(milis)
    except:
        continue
    if(len(hrValues)==100):
            #analisisHR()
            hrValues=hrValues[25:]
            miliValues=miliValues[25:]
            analisisHR()