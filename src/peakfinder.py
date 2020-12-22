def peakfinder(data):
    peaks = []
    xbin = 10
    for i in range(len(time)-1):
        if data[i]>data[i+1] and data[i]>data[i-1] and data[i]>data[i+xbin] and data[i]>data[i-xbin]:
            peaks.append(data[i])
    return peaks
'''
 This simple peakfinder algorithm works on sufficiently smoothed data, although 
 parameters can be altered to make it work for different data sets.
 The rather cumbersome "if" condition finds all local maxima, and then filters
 for maxima within the set bin, which can be chosen by eyeballing data to figure out 
 which peaks are statistically significant and estimating the necessary width
 
 '''