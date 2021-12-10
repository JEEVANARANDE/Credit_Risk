#load the train and test data
#train algo
#save the metrics and params

import os
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.metrics import roc_curve, f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import pickle
import os
import warnings
import matplotlib.pyplot as plt
import json
import joblib
import argparse



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    parsed_args = args.parse_args()
    #ConnectDB().casandra_to_local_get_data(config_path=parsed_args.config)
    split_and_save_data(config_path=parsed_args.config)