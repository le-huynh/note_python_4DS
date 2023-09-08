# given the name of a swimmer's file, 
# extract all the required data, 
# then return it to the caller as a tuple

import statistics
from pyprojroot.here import here

def get_swim_data(folder, filename):
    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")

    with open(here(folder + filename)) as df:
        data = df.readlines()
    times = data[0].strip().split(",")

    converts = []
    for value in times:
        if ":" in value:
            minutes, rest = value.split(":")
            seconds, hundredths = rest.split(".")
        else:
            minutes = 0
            seconds, hundredths = value.split(".")
        converts.append(int(minutes)*60*100 + int(seconds)*100 + int(hundredths))
    
    average = statistics.mean(converts)
    mins_secs, hundredths = str(round(average/100, 2)).split(".")
    mins_secs = int(mins_secs)
    minutes = mins_secs//60
    seconds = mins_secs - minutes*60
    average_str = str(minutes) + ":" + str(seconds) + "." + hundredths
    
    return swimmer, age, distance, stroke, average, average_str, times