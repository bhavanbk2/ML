# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 00:09:17 2023

@author: 016775421
"""

import numpy as np
import joblib
import pandas as pd
import streamlit as st

loaded_model=joblib.load('Desktop/voting_classifier_model.joblib')

def intrusion_prediction(input_data):
    X_test=pd.read_csv('Desktop/test.csv')
    X_test.info()
    pred=loaded_model.predict(X_test)
    print("Count of Malicious DDoS:", (pred == 0).sum(), "times")
    print("Count of Non Malicious DDoS:", (pred == 1).sum(), "times")
  
    
  
def main():
    
    
    # giving a title
    st.title('DDoS Prediction')
    
    
    # getting the input data from the user
    # option to choose input method (manual input or file upload)
    input_method = st.radio("Select Input Method", ["Manual Input", "File Upload"])
    
    if input_method == "Manual Input":
        # getting the input data from the user
        types = st.text_input('Number of types',type='int')
        id_orig_addr = st.text_input('id.orig_addr',type='float')
        id_resp_haddr = st.text_input('id.resp_haddr',type='float')   
        missed_bytes_count= st.text_input('missed_bytes_count',type='float')
        orig_pkts_count = st.text_input('orig_pkts_count',type='float')
        orig_ip_bytes_count = st.text_input('orig_ip_bytes_count',type='float')
        resp_pkts_count = st.text_input('resp_pkts_count',type='float')
    
        # Perform prediction or other processing based on manual input
    elif input_method == "File Upload":
        # file upload widget
        uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

        if uploaded_file is not None:
            # Read the uploaded file into a Pandas DataFrame
            X_test = pd.read_csv(uploaded_file)

            # Display the DataFrame
            st.write("Uploaded DataFrame:")
            st.write(X_test)

            # Perform prediction or other processing based on the uploaded file
            # ...
    
    # code for Prediction
    Prediction = ''
    
    # creating a button for Prediction
    
    if st.button('Network intrusion Test Result through file upload'):
        Prediction = intrusion_prediction(X_test)
    else:
        Prediction = intrusion_prediction([types,id_orig_addr,id_resp_haddr,missed_bytes_count,orig_pkts_count,orig_ip_bytes_count,resp_pkts_count])
        
        
    st.success(Prediction)
    
    
    
    
    
if __name__ == '__main__':
    main()