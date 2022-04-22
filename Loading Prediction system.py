import numpy as np
import pickle
from pip import main
import streamlit as st
from PIL import Image


loaded_model = pickle.load(open('D:/Project/trained_model.sav', 'rb'))



input_data = (3, 1, 0, 12.611538, 339, 12.537641, 102898.630140, 0)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
y_pred = loaded_model.predict(input_data_reshaped)
print(y_pred)

if (y_pred[0] == 0):
    print("The policy will not have a premium loading")
else:
    print("The policy will have a premium loading")
