from pprint import pprint
from typing import Dict, Callable

import lightgbm as lgb
import numpy as np
from econml import dml, metalearners
from sklift.metrics import uplift_at_k

from src.datasets_ import split_datasets, X5Dataset


def validate_econml(df_features,
                    treatment,
                    y,
                    model,
                    metrics: Dict[str,
                                  Callable[[np.ndarray, np.ndarray, np.ndarray], float]]
                    ):
    train_triplet, test_triplet = split_datasets(df_features, treatment, y)
    model.fit(*train_triplet)

    scores = dict()
    y_valid, treat_valid, X_valid = test_triplet
    uplift = np.squeeze(model.effect(X_valid.values))

    for key, metric in metrics.items():
        scores[key] = metric(y_true=y_valid, uplift=uplift, treatment=treat_valid)

    return scores


if __name__ == "__main__":

    metrics = {
        'uplift_at_30_by_group': lambda **kwargs: uplift_at_k(**kwargs, strategy="by_group", k=0.3)
    }

    models = (
        # dml.LinearDMLCateEstimator(model_y=lgb.LGBMClassifier(max_depth=5),
        #                            model_t=lgb.LGBMClassifier(max_depth=5),
        #                            discrete_treatment=True),
        # dml.NonParamDMLCateEstimator(model_y=lgb.LGBMRegressor(),
        #                              model_t=lgb.LGBMRegressor(),
        #                              model_final=lgb.LGBMRegressor()),
        metalearners.TLearner(lgb.LGBMRegressor(subsample=0.35, max_depth=2)),
        metalearners.XLearner(lgb.LGBMRegressor(subsample=0.35, max_depth=2)),
        metalearners.SLearner(lgb.LGBMRegressor(subsample=0.35, max_depth=2)),
        # metalearners.TLearner(lgb.LGBMClassifier(subsample=0.35, max_depth=2)),
        # metalearners.XLearner(lgb.LGBMClassifier(subsample=0.35, max_depth=2)),
        # metalearners.SLearner(lgb.LGBMClassifier(subsample=0.35, max_depth=2)),
    )

    dataset = X5Dataset("../data/x5-retail-hero")
    data = dataset.get_data()

    for model in models:
        print(model)
        n_cv = 5

        scores = dict()
        for i in range(n_cv):
            for key, value in validate_econml(*data, model, metrics).items():
                scores[key] = scores.get(key, 0) + value
                print(key, value)
        for key, value in scores.items():
            scores[key] /= n_cv

        pprint(scores)
        print("="*100)
