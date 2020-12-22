def peakfinder(data):
    peaks = []
    for i in range(len(data)):
        if data[i]>data[i+1] and data[i]>data[i-1] and i+1 < len(data):
            peaks.append(data[i])
    return peaks