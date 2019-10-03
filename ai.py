import numpy as np
import pandas as pd

from tensorflow.keras.models import Model
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import RMSprop, Adam

from datetime import datetime
import itertools
import argparse
import re
import os
import pickle

from sklearn.preprocessing import StandardScaler

def getTrainingDataFromFile():
    data = pd.read_csv('Google_Stock_Price_Train.csv')
    data = data.iloc[:,1:2]
    return data.values

class Agent(object):
    def __init__():
    
