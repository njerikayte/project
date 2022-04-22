import numpy as np
import pickle
from pip import main
import streamlit as st
from PIL import Image

import os

working_dir = os.path.dirname(__file__)
print(working_dir)
loaded_model = pickle.load(open(working_dir+'/trained_model.sav', 'rb'))


#creating a function for prediction

def loading_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    y_pred = loaded_model.predict(input_data_reshaped)
    print(y_pred)

    if (y_pred[0] == 0):
        return"According to our calculations, the policy will not have a premium loading"
    else:
        return"According to our calculations, the policy will have a premium loading"


def main():
    img1 = Image.open(working_dir+'/logo.PNG')
    #img1 = img1.resize((156,145))
    st.image(img1,use_column_width=False)
    
    #giving a title
    st.title('Premium Loading Prediction Web App ')
    
    
    #getting the input data from the user

    PRINCIPAL_NAME = st.text_input('Principal Member Name')

    #fam size
    FAMSIZE_DISPLAY = ('None', 'One', 'Two', 'Three', 'Four', 'Five', 'Six')
    FAMSIZE_OPTIONS = list(range(len(FAMSIZE_DISPLAY)))
    FAMSIZE_NAME = st.selectbox("No of Dependents",FAMSIZE_OPTIONS, format_func=lambda x: FAMSIZE_DISPLAY[x])



    #for scheme
    SCHEME_NAME_DISPLAY = ('Budget', 'Executive', 'Ignite', 'Premier')
    SCHEME_NAME_OPTIONS = list(range(len(SCHEME_NAME_DISPLAY)))
    SCHEME_NAME = st.selectbox("Scheme Name",SCHEME_NAME_OPTIONS, format_func=lambda x: SCHEME_NAME_DISPLAY[x])


    #CHRONIC_OR_NOT = st.text_input('Any Chronic illness?')
    CHRONIC_OR_NOT_DISPLAY = ('No', 'Yes')
    CHRONIC_OR_NOT_OPTIONS = list(range(len(CHRONIC_OR_NOT_DISPLAY)))
    CHRONIC_OR_NOT = st.selectbox("Do you have any Chronic Illness?",CHRONIC_OR_NOT_OPTIONS, format_func=lambda x: CHRONIC_OR_NOT_DISPLAY[x])
    
    
    #TYPE_OF_PROVIDER = st.text_input('Which provider do you prefer, Tier I, Tier II or Both?')
    TYPE_OF_PROVIDER_DISPLAY = ('Tier I', 'Tier II', 'Both Tier I and Tier II')
    TYPE_OF_PROVIDER_OPTIONS = list(range(len(TYPE_OF_PROVIDER_DISPLAY)))
    TYPE_OF_PROVIDER = st.selectbox("Which type of providers do you prefer?",TYPE_OF_PROVIDER_OPTIONS, format_func=lambda x: TYPE_OF_PROVIDER_DISPLAY[x])


    INVOICED_PREMIUMS = st.number_input("Premiums Paid",value=0)
    EARNED_DAYS = st.number_input("Cover Duration in Days",min_value=305)
    EARNED_PREMIUMS = st.number_input("Earned Premiums",value=0)
    total_claims = st.number_input("Total Claims Incurred",value=0)

    #autocalculation of loss ratio
    #loss_ratio = st.number_input("Loss Ratio",value=total_claims/INVOICED_PREMIUMS)
    
    #def Div(total_claims,INVOICED_PREMIUMS):
      #  if total_claims == 0:
       #     return 0
       # else: Div(1 + total_claims,INVOICED_PREMIUMS)
   # print(Div(total_claims,INVOICED_PREMIUMS))
    
    loss_ratio = st.text_input("Loss Ratio")


    #code for Prediction
    loading = ''

    #creating a button for prediction
    if st.button('Submit'):
        loading = loading_prediction([SCHEME_NAME, CHRONIC_OR_NOT, TYPE_OF_PROVIDER, INVOICED_PREMIUMS, EARNED_DAYS, EARNED_PREMIUMS, total_claims, loss_ratio])

    st.success(loading)


if __name__ == '__main__':
    main()