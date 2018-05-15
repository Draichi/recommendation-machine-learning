# activate virtual env:
# $ source ~/tensorflow/bin/activate
#
# desactivate virtual env:
# $ deactivate

import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM
from lightfm.evaluation import precision_at_k, auc_score

data = fetch_movielens(min_rating=3.0)

model = LightFM(loss='warp', learning_rate=0.05)
model.fit(data['train'], epochs=200, num_threads=3)

# Measure the precision at k metric for a model: 
# the fraction of known positives in the first k positions
# of the ranked list of results. A perfect score is 1.0.
test_precision_at_k = precision_at_k(model, data['test'], k=3).mean()

# Measure the ROC AUC metric for a model: the probability that 
# a randomly chosen positive example has a higher score than a 
# randomly chosen negative example. A perfect score is 1.0.
test_auc_score      = auc_score(model, data['test']).mean()

print('-- Precision at k:', test_precision_at_k)
print('-- AUC score:', test_auc_score)

def sample_recommendation(model, data, user_ids):
    n_users, n_items = data['train'].shape

    for user_id in user_ids:
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        scores = model.predict(user_id, np.arange(n_items))
        top_items = data['item_labels'][np.argsort(-scores)]

        print('\nuser %s' % user_id)
        print('known positives:')

        for x in known_positives[:3]:
            print('     %s' % x)

        print('recommended:')

        for x in top_items[:3]:
            print('     %s' % x)

sample_recommendation(model, data, [79, 80, 41])
