import numpy as np
import pickle
import pandas as pd
import streamlit as st

model_filename = 'Desktop/voting_classifier_model.pkl'

with open(model_filename, 'rb') as file:
    loaded_model = pickle.load(file)

def intrusion_prediction(X_test):
    pred = loaded_model.predict(X_test)
    malicious_count = (pred == 0).sum()
    non_malicious_count = (pred == 1).sum()
    return malicious_count, non_malicious_count

def main():
    # Set page title and icon
    st.set_page_config(page_title="DDoS Prediction App", page_icon="🛡️")

    # Header
    st.title('DDoS Prediction App')
    st.subheader('Upload a CSV file to predict network intrusion')

    # File Upload
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the uploaded file into a Pandas DataFrame
        X_test = pd.read_csv(uploaded_file)

        # Display the DataFrame
        st.write("Uploaded DataFrame:")
        st.dataframe(X_test)

        # Perform prediction or other processing based on the uploaded file
        # ...

        # Prediction Button
        if st.button('Predict Network Intrusion'):
            malicious_count, non_malicious_count = intrusion_prediction(X_test)

            # Display Results
            st.success("Prediction Results:")
            st.info(f"Count of Malicious DDoS: {malicious_count} times")
            st.info(f"Count of Non-Malicious DDoS: {non_malicious_count} times")

if __name__ == '__main__':
    main()
