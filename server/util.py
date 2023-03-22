import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, total_sqft, bedroom, ready_to_move):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bedroom
    x[2] = ready_to_move
    if loc_index >= 0:
        x[loc_index] = 1 
    
    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open('./artifacts/bangalore_house_price_perdiction_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('loading saved artifacts... done')

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1875, 3, 0))
    print(get_estimated_price('1st Phase JP Nagar', 1875, 2, 1))
    print(get_estimated_price('Munich', 1394, 2, 1))
    print(get_estimated_price('Deggendorf', 1394, 2, 1))

    