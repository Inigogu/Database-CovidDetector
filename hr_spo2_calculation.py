import matplotlib.pyplot as plt, numpy as np, random
from scipy.signal import find_peaks

# HR 35-36 sin dedo, 720-750 con dedo
# RED 200k +-500 sin dedo, 233k +-500 con dedo
# IR 2200+-100 sin dedo,  220500 +- 100 con dedo
# milis - tiempo en milisegundos
def sensorValue(min = 200000, max = 233000, range = 500, with_finger = False):
    return random.randint(max, max+range) if with_finger else random.randint(min, min+range)

def smooth_curve_simple(points, sample_size):
    # smoothed_points = [sum(points[i:i+sample_size])/sample_size for i in range(0, len(points), sample_size)]
    # print(len(smoothed_points))
    # return smoothed_points
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

def analisisHR(hrValues, miliValues, sample_size):
    smoothed_values =[ data for data,i in smooth_curve_simple(hrValues, sample_size)]
    peaks = find_peaks(smoothed_values)[0]

    valorHR=(60000*len(peaks))/(miliValues[-1]-miliValues[0])

    return valorHR

hrValues=[]
miliValues=[]
redValues=[]
irValues=[]

random.seed(0)
milis = 0

while(len(hrValues) < 500):
    hrValues.append(random.randint(720, 750))
    miliValues.append(milis)
    milis += random.randint(125, 150)

print(miliValues[-1])
hr = analisisHR(hrValues, miliValues, 2)
print(hr)
