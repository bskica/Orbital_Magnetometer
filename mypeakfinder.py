def peakfinder(data):
    peaks = []
    for i in range(len(data)):
        if i > 0 and i < (len(data)-2):
            if (data[i-1] < data[i]) and (data[i+1] < data[i]):
                peaks.append(data[i])
    return peaks
