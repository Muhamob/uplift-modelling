import pandas as pd
from tqdm import tqdm

import json


def to_json(df):
    def _f(x):
        transactions = x.groupby("transaction_id")
	records = {
	    "client_id": x.client_id.iloc[0],
	    "transactions": transactions.agg({
		'transaction_id': 'first',
		'transaction_datetime': 'first',
		'regular_points_received': 'first',
		'express_points_received': 'first',
		'regular_points_spent': 'first', 
		'express_points_spent': 'first',
		'purchase_sum': 'first',
		'store_id': 'first',
		'product_id': lambda x: x.tolist(),
		'product_quantity': lambda x: x.tolist(),
	    }).to_dict(orient="records")
	}
	return records

    for line in tqdm(df.groupby("client_id").apply(_f).to_list()):
        yield line


def to_jsonl(df: pd.DataFrame, output_path: str):
    print("Start writing result to file")
    with open(output_path, "w") as file_:
        for line in to_json(df):
            file_.write(json.dumps(line)+"\n")
    print("[done] stop writing to jsonl")

