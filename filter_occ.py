import streamlit as st
from  src import  analysis_freq as filter_freq
import pandas as pd


def read_file(file):
    if file.name.endswith('xlsx'):
        return filter_freq.Analysis_frequency(file)


def perform_analysis(file,option):
    df = read_file(file)
    if df is None:
        st.write("Unsupport file type")
        return
    if option == "Frequency usage":
        return df.freq_usage()
    elif option == "Frequency Maybe illegal":
        return df.ferq_illegal()
    elif option == "Frequency should delete":
        return df.should_delete()
    



def main():
    st.write('Hello, *NBTC!* :sunglasses:')

    upload_files = st.file_uploader("Upload Files",type=['xlsx'],accept_multiple_files=True)
    option = st.selectbox('Select option for filter',('Frequency usage','Frequency Maybe illegal','Frequency should delete'))
    
    if upload_files:
        for uploaded_file in upload_files:
            result = perform_analysis(uploaded_file,option)
            st.write(f"Result for {uploaded_file.name}")
            st.write(result)





if __name__ == "__main__":
    main()