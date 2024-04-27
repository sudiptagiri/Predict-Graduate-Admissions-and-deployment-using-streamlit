# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 21:28:20 2024

@author: hp
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def Predict_Graduate_Admissions(gre,toefl,rating,sop,lor,gpa,research):
    
    """Let's Predict graduate admission 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: gre
        in: query
        type: number
        required: true
      - name: toefl
        in: query
        type: number
        required: true
      - name: rating
        in: query
        type: number
      required: true
      - name: sop
        in: query
        type: number
        required: true
      - name: lor
        in: query
        type: number
        required: true
      - name: gpa
        in: query
        type: number
        required: true
      - name: research
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[gre,toefl,rating,sop,lor,gpa,research]])
    print(prediction)
    return prediction



def main():
    st.title("Predict Graduate Admissions")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit graduate admission predictor ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    gre = st.text_input("gre","Type Here")
    toefl = st.text_input("toefl","Type Here")
    rating = st.text_input("rating","Type Here")
    sop = st.text_input("sop","Type Here")
    lor = st.text_input("lor","Type Here")
    gpa = st.text_input("gpa","Type Here")
    research = st.text_input("research","Type Here")
    
    result=""
    if st.button("Predict"):
        result=Predict_Graduate_Admissions(gre,toefl,rating,sop,lor,gpa,research)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()