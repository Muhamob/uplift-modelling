import os
from abc import ABC, abstractmethod
from typing import Union, Tuple, Dict, Callable

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

PathType = Union[str, os.PathLike]


class Dataset(ABC):
    @abstractmethod
    def get_data(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        Return prepared data in form of
        :return: (train_features, treatment, target)
        """
        pass

    @abstractmethod
    def get_features(self, *args, **kwargs) -> pd.DataFrame:
        """
        Transform inputs to produce features
        :return: pd.DataFrame
        """
        pass


class X5Dataset(Dataset):
    def __init__(self, dir_path: PathType):
        self.dir_path = dir_path

    def get_features(self, df_clients: pd.DataFrame, df_train: pd.DataFrame) -> pd.DataFrame:
        df_features = df_clients.copy()
        df_features['first_issue_time'] = (pd.to_datetime(df_features['first_issue_date'])
                                           - pd.to_datetime(df_features['first_issue_date']).min()) / pd.Timedelta('365d')
        df_features['first_redeem_time'] = (pd.to_datetime(df_features['first_redeem_date'])
                                            - pd.to_datetime(df_features['first_redeem_date']).min()) / pd.Timedelta('365d')
        df_features['issue_redeem_delay'] = df_features['first_redeem_time'] - df_features['first_issue_time']

        df_features = df_features.join(pd.get_dummies(df_features['gender']))
        df_features['first_redeem_time'] = df_features['first_redeem_time'].fillna(
            df_features['first_redeem_time'].mean())
        df_features['issue_redeem_delay'] = df_features['issue_redeem_delay'].fillna(
            df_features['issue_redeem_delay'].mean())

        df_features = df_features.drop(['first_issue_date', 'first_redeem_date', 'gender'], axis=1)

        return df_features

    def load_df_clients(self) -> pd.DataFrame:
        return pd.read_csv(os.path.join(self.dir_path, "clients.csv"), index_col='client_id')

    def load_df_train(self) -> pd.DataFrame:
        return pd.read_csv(os.path.join(self.dir_path, "uplift_train.csv"), index_col='client_id')

    def get_data(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        # load dataframes
        df_clients = self.load_df_clients()
        df_train = self.load_df_train()

        # prepare features
        df_features = self.get_features(df_clients, df_train)
        y = df_train['target']
        treatment = df_train['treatment_flg']

        return df_features, treatment, y


def split_datasets(df_features: pd.DataFrame, treatment: pd.DataFrame, y: pd.DataFrame):
    indices = treatment.index
    indices_train, indices_valid = train_test_split(indices, test_size=0.5)

    X_train = df_features.loc[indices_train, :]
    y_train = y.loc[indices_train]
    treat_train = treatment.loc[indices_train]

    X_valid = df_features.loc[indices_valid, :]
    y_valid = y.loc[indices_valid]
    treat_valid = treatment.loc[indices_valid]

    return [(y_train, treat_train, X_train), (y_valid, treat_valid, X_valid)]
