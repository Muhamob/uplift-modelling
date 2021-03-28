from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Client(Base):
    __tablename__ = "clients"

    client_id = Column(String, primary_key=True)
    first_issue_date = Column(DateTime, nullable=True)
    first_redeem_date = Column(DateTime, nullable=True)
    age = Column(Integer)
    gender = Column(String)

    purchases = relationship('Purchase')


class Purchase(Base):
    __tablename__ = 'purchases'

    id = Column(Integer, primary_key=True)
    client_id = Column(String, ForeignKey('clients.client_id'))
    transaction_id = Column(String)
    transaction_datetime = Column(DateTime)
    regular_points_received = Column(Float)
    express_points_received = Column(Float)
    regular_points_spent = Column(Float)
    express_points_spent = Column(Float)
    purchase_sum = Column(Float)
    store_id = Column(String)
    product_id = Column(String)
    product_quantity = Column(Float)
    trn_sum_from_iss = Column(Float)
    trn_sum_from_red = Column(Float)


# if __name__ == "__main__":
    # from src.config.base import ROOT_DIR
    # from tqdm import tqdm
    # from sqlalchemy import create_engine
    # from sqlalchemy.orm import sessionmaker
    # import pandas as pd
    #
    # engine = create_engine("postgresql://admin:admin@localhost:5432/x5")
    # conn = engine.connect()
    #
    # Base.metadata.create_all(engine)

    # df_clients = pd.read_csv(ROOT_DIR / 'data/datasets/x5-retail-hero/clients.csv.gz')
    # df_clients['first_issue_date'] = pd.to_datetime(df_clients['first_issue_date'])
    # df_clients['first_redeem_date'] = pd.to_datetime(df_clients['first_redeem_date'])

    # Session = sessionmaker(bind=engine)
    # session = Session()
    # for i, row in tqdm(enumerate(df_clients.iterrows()), total=df_clients.shape[0]):
    #     val = row[1].to_dict()
    #     val = {k:None if isinstance(v, float) else v for k,v in val.items()}
    #     session.add(Client(**val))
    # session.commit

    # df_purchases = pd.read_csv(ROOT_DIR / 'data/datasets/x5-retail-hero/purchases.csv.gz')
    # df_purchases.fillna(0, inplace=True)
    #
    # batch_size = 10_000
    # for i, row in tqdm(enumerate(df_purchases.iterrows()), total=df_purchases.shape[0]):
    #     val = row[1].to_dict()
    #     session.add(Purchase(**val))
    #     if i % batch_size == batch_size - 1:
    #         session.commit()
    #
    # session.commit()
    # session.close()
