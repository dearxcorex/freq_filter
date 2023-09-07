import streamlit as st
import pandas as pd
import time
from st_pages import Page,show_pages,add_page_title


df  =  pd.read_csv("csv/VHF-05.csv")
st.title("Database of VHF")



st.write('Hello, *World!* :sunglasses:')

def search_freq_range(freq_start_stop):

    freq_start_stop = freq_start_stop.split("-")

    #only one value
    if len(freq_start_stop) == 1:
        freq_start = float(freq_start_stop[0])
        freq_search = df["คลื่นความถี่ (MHz)"] == freq_start
        df_search = df[freq_search]

    elif len(freq_start_stop) == 2:
        freq_start = float(freq_start_stop[0])
        freq_stop = float(freq_start_stop[1])
        freq_search_range = df["คลื่นความถี่ (MHz)"].between(freq_start, freq_stop)
        df_search = df[freq_search_range]

    else:
        return st.write("Error")

    return df_search


freq_start_stop = st.text_input("Enter a frequency range", value="108.0-450.0")
df_search = search_freq_range(freq_start_stop)

st.write(df_search)





