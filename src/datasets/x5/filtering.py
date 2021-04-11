import pandas as pd

from pathlib import Path


if __name__ == "__main__":
    dataset_path = Path("../../../data")
    
    df_purchases = pd.read_csv(dataset_path / 'datasets/x5-retail-hero/purchases.csv.gz', infer_datetime_format=True)
    df_train = pd.read_csv(dataset_path / "datasets/x5-retail-hero/uplift_train.csv.gz", index_col="client_id")

    indices = df_purchases[["client_id", ]].set_index("client_id").index.intersection(df_train.index)

    df_purchases.set_index("client_id").loc[indices].to_csv(dataset_path / "interim/purchases_filtered.csv.gz", index=True, compression="gzip")




