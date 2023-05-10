# <YOUR_IMPORTS
import glob
import dill
import os
import pandas as pd
import json
from datetime import datetime

path = os.environ.get('PROJECT_PATH', '.')
model_filename = glob.glob(f'{path}/data/models/*.pkl')
#model_filename = f'./{path}/data/models/cars_pipe_202305030953.pkl'
jsons = ['7310993818.json', '7313922964.json',
         '7315173150.json', '7316152972.json',
         '7316509996.json']


def read_model():
    with open(model_filename[-1], 'rb') as file:
        result = dill.load(file)
        return result


def create_df(dict_):
    df_pred = pd.DataFrame(columns=['id', 'pred'])
    df_z = pd.DataFrame(dict_)
    df_pred = pd.concat([df_pred, df_z], axis=0)
    df_pred.to_csv(f'{path}/data/predictions/preds_{datetime.now().strftime("%Y%m%d%H%M")}.csv')


def predict():
    z = {}
    model = read_model()
    for i in jsons:
        with open(f'{path}/data/test/{i}') as fin:
            form = json.load(fin)
            df = pd.DataFrame.from_dict([form])
            y = model.predict(df)
            z = {'id': df.id, 'pred': y}
            create_df(z)


if __name__ == '__main__':
    predict()
