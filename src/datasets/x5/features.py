import pandas as pd
from scipy import stats
import numpy as np
from tqdm import tqdm

import json
from datetime import datetime
from pprint import pprint
from typing import List, Dict, Tuple, Sequence, Iterable


def loader(path: str):
    with open(path, "r") as f:
        for line in f.readlines():
            yield json.loads(line)


def show_example(path: str):
    for line in loader(path):
        pprint(line)
        break


def dates_features(history: Sequence[dict]):
    dates = pd.Series([datetime.strptime(t["transaction_datetime"], "%Y-%m-%d %H:%M:%S") for t in history])
    
    dayweek_count = dates.groupby(dates.dt.dayofweek).count()
    dayweek_count /= dayweek_count.sum()
    dayweek_count = dayweek_count.to_dict()
    
    month_count = dates.groupby(dates.dt.month).count()
    month_count = month_count.to_dict()
    
    return {
        **{f"percent_of_transactions_in_{i}_day": dayweek_count.get(i, 0) for i in range(0, 7)},
        **{f"percent_of_transactions_in_{i}_month": month_count.get(i, 0) for i in range(1, 13)}
    }


def transaction_features(transaction_history: Sequence[dict]):
    loyalty_points_names = [
        'regular_points_received',
        'express_points_received',
        'regular_points_spent', 
        'express_points_spent',
        'purchase_sum'
    ]
    features = dict()
    
    def distr_field(name):
        return {
            f'{name}_mean': np.mean([i[field] for i in transaction_history]),
            f'{name}_std': np.std([i[field] for i in transaction_history]),
            f'{name}_median': np.median([i[field] for i in transaction_history]),
            f'{name}_max': np.max([i[field] for i in transaction_history]),
            f'{name}_skew': stats.skew([i[field] for i in transaction_history]),
            f'{name}_last': transaction_history[-1][field]
        }
    
    for field in loyalty_points_names:
        features.update(distr_field(field))
        
    def dates(history):
        dates = [datetime.strptime(t["transaction_datetime"], "%Y-%m-%d %H:%M:%S") for t in transaction_history]
        return {
            'mean_transactions_in_month': np.mean()
        }

    # features.update(dates(transaction_history))
        
    return features


def extract_features(path: str):
    for line in tqdm(loader(path)):
        features = transaction_features(line['transactions'])
        features.update(dates_features(line['transactions']))
        del line['transactions']
        line.update(features)
        yield line


def extract_features_to_file(path: str, output_path: str):
    # TODO: add line by line feature-extraction -> writing to csv file without using pd.DataFrame
    pd.DataFrame.from_records(extract_features(path)).set_index("client_id").to_csv(output_path, index=True)


def extract_user_features(df_clients_path: str):
    df_features = pd.read_csv(df_clients_path, index_col="client_id")
    
    df_features['first_issue_time'] = \
	(pd.to_datetime(df_features['first_issue_date'])
	 - pd.to_datetime(df_features['first_issue_date']).min()) / pd.Timedelta('365d')

    df_features['first_redeem_time'] = \
	(pd.to_datetime(df_features['first_redeem_date'])
	 - pd.to_datetime(df_features['first_redeem_date']).min()) / pd.Timedelta('365d')

    df_features['issue_redeem_delay'] = df_features['first_redeem_time'] \
                - df_features['first_issue_time']

    df_features = df_features.join(pd.get_dummies(df_features['gender']))

    df_features['first_redeem_time'] = df_features['first_redeem_time'].fillna(df_features['first_redeem_time'].mean())
    df_features['issue_redeem_delay'] = df_features['issue_redeem_delay'].fillna(df_features['issue_redeem_delay'].mean())

    df_features = df_features.drop(['first_issue_date', 'first_redeem_date', 'gender'], axis=1)

    return df_features


def extract_user_features_to_file(path: str, output_path: str):
    extract_user_features(path).to_csv(output_path, index=True)
