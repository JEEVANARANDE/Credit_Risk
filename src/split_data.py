#split the raw data 
# save it in data/processed folder

import os
import argparse
import pandas as pd
from data_preprocessing import *
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_and_save_data(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    raw_data_path = config["Feature_extraction"]["x_indept_scaled_var"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]
    X,y=Feature_extraction(config_path)
    print(type(X), type(y))
    df = X.merge(pd.DataFrame(y), how='left', left_index=True, right_index=True)
    #df = pd.read_csv(raw_data_path,sep=",")
    train,test = train_test_split(df,test_size=split_ratio,random_state=random_state)
    train.to_csv(train_data_path,sep=",",index=False)
    test.to_csv(test_data_path,sep=",",index=False)



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    parsed_args = args.parse_args()
    #ConnectDB().casandra_to_local_get_data(config_path=parsed_args.config)
    split_and_save_data(config_path=parsed_args.config)