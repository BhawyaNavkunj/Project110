import csv
from os import stat
import pandas as pd 
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()

population_mean = statistics.mean(data)
print("Population mean : ",population_mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["claps"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    sampling_mean = statistics.mean(mean_list)
    print("Sampling mean : ",sampling_mean)
setup()