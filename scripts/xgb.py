#!/usr/bin/python

'''
Martin Kersner, m.kersner@gmail.com
2015/12/26
'''

import xgboost as xgb

def init_xgb_train_data(target, data):
    return xgb.DMatrix(data, label=target)

def init_xgb_test_data(data):
    return xgb.DMatrix(data)

def init_xgb_parameters():
    param = {'bst:max_depth':2, 'bst:eta':1, 'silent':1, 'objective':'binary:logistic' }
    param['nthread'] = 4
    param['eval_metric'] = 'auc'

    return param.items()

def train_xgb(y_train, X_train, settings):
    dtrain = init_xgb_train_data(y_train, X_train)
    num_round = settings['num_round']

    evallist  = [(dtrain, 'train')]
    plst = init_xgb_parameters()
    bst = xgb.train(plst, dtrain, num_round, evallist)

    return bst

def train_val_xgb(y_train, X_train, y_val, X_val, settings):
    dtrain = init_xgb_train_data(y_train, X_train)
    dtest  = init_xgb_train_data(y_val, X_val)
    evallist  = [(dtest, 'eval'), (dtrain, 'train')]

    num_round = settings['num_round']
    plst = init_xgb_parameters()
    bst = xgb.train(plst, dtrain, num_round, evallist)

    return bst

def predict_xgb(bst, data):
    dtest = init_xgb_test_data(data)
    return bst.predict(dtest)

def save_model():
    pass