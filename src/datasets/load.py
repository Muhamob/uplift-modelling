import json
import os
import math
import csv

from pymongo import MongoClient
import pandas as pd
import numpy as np
from tqdm import tqdm


client = MongoClient("localhost", 27017)


def clean_document_from_nan(doc: dict) -> dict:
    for field, value in list(doc.items()):
        if isinstance(value, float) and math.isnan(value):
            del doc[field]
    return doc


def load_clients(path, db):
    print(f"Start loading {path}")
    df = pd.read_csv(path)
    docs = []

    for doc in tqdm(df.to_dict("records")):
        doc = clean_document_from_nan(doc)
        docs.append(doc)

    db['clients'].insert_many(docs)


def load_products(path, db):
    print(f"Start loading {path}")
    df = pd.read_csv(path)
    docs = []

    for doc in tqdm(df.to_dict("records")):
        doc = clean_document_from_nan(doc)
        docs.append(doc)

    db['products'].insert_many(docs)


def load_uplift(path, db):
    print(f"Start loading {path}")
    df = pd.read_csv(path)
    docs = []

    for doc in tqdm(df.to_dict("records")):
        doc = clean_document_from_nan(doc)
        docs.append(doc)

    db['uplift'].insert_many(docs)


def load_check_queries(path, db):
    print(f"Start loading {path}")
    df = pd.read_csv(path, sep="\t", header=None)

    docs = []

    for doc in tqdm(df.iloc[:, 0]):
        doc_dict = clean_document_from_nan(json.loads(doc))
        docs.append(doc_dict)

    db['check_queries'].insert_many(docs)


def load_purchases(path, db):
    print(f"Start loading {path}")
    batch_size = 500_000
    with open(path, 'r') as f:
        reader = csv.DictReader(f, delimiter=",")
        docs = []

        for i, doc in tqdm(enumerate(reader)):
            docs.append(clean_document_from_nan(doc))
            if i % batch_size == batch_size - 1:
                db['purchases'].insert_many(docs)
                docs = []
        if len(docs) != 0:
            db['purchases'].insert_many(docs)


def load_x5(path_to_dir):
    db = client['x5']
    load_purchases(os.path.join(path_to_dir, "purchases.csv"), db)
    load_uplift(os.path.join(path_to_dir, "uplift_train.csv"), db)
    load_clients(os.path.join(path_to_dir, "clients.csv"), db)
    load_products(os.path.join(path_to_dir, "products.csv"), db)
    load_check_queries(os.path.join(path_to_dir, "check_queries.tsv"), db)


if __name__ == "__main__":
    client['x5'].command("dropDatabase")
    load_x5("../../data/x5-retail-hero")
