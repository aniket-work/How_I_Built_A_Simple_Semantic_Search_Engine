import pandas as pd

def load_data(config):
    df = pd.read_csv(config['data']['csv_path'])
    df['id'] = df.index
    return df.head(config['data']['subset_size'])