import pandas as pd


def load_df(path):
    """
    Path to data/ dir
    """
    transaction_features = pd.read_csv(path + "preprocessed/x5_transaction_features.csv", index_col="client_id")
    client_features = pd.read_csv(path + "preprocessed/x5_client_features.csv", index_col="client_id")
    df_target = pd.read_csv(path+"datasets/x5-retail-hero/uplift_train.csv.gz", index_col="client_id")
    df = transaction_features.join(client_features).join(df_target)
    df


