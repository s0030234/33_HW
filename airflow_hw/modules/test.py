import glob
import os
import dill

path = os.environ.get('PROJECT_PATH', '..')
model_filename = glob.glob(f'./{path}/data/models/*.pkl')[-1]

def predict():
    print(model_filename)
    with open(model_filename, 'rb') as file:
        result = dill.load(file)
    print(result)

if __name__ == '__main__':
    predict()