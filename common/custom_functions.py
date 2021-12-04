import pandas as pd
import yaml

def pandas_factory(colnames, rows):
        return pd.DataFrame(rows, columns=colnames)

def read_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config