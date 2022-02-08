# import _crypt

from importlib.resources import path
# import numpy as np
import pandas as pd
import openpyxl

from flask import *
import json, time


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home_page():
    data_set = {'Page':'Home', 'Message':'te conectaste exitosamente', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump



# year = 2020
# mes = "B" 
# dia = 28 - 1


# path= f'{year}.xlsx'
# #leemos el excel usando pandas
# valor = pd.read_excel(path, usecols= mes, header= dia, nrows=0, index_col=None)
# data = valor.columns.values[0]
# print (data)

# if __name__ == '__main__':
#     app.run(port=7777)

