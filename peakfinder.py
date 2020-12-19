def peakfinder(data):
    current = data[int((len(data) / 2))]
    if len(data) == 1:
        return current
    elif current == data[0] and current >= data[1]:
        return current
    elif current == data[len(data) - 1] and current >= data[len(data) - 2]:
        return current
    elif current < data[int((len(data) / 2)) - 1]:
        data = data[0:int(len(data) / 2)]
        return peakfinder(data)
    else:
        data = data[int(len(data) / 2): len(data) - 1]
        return peakfinder(data)