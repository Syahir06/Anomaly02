import streamlit as st
import pandas as pd
from tv_scheduling_ga import run_ga  # assuming your GA code is in tv_scheduling_ga.py

# Title
st.title("TV Scheduling using Genetic Algorithm")

# Upload modified CSV file
uploaded_file = st.file_uploader("Upload Modified Ratings CSV", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of Data:")
    st.dataframe(data)

    # GA parameters input
    st.sidebar.header("Genetic Algorithm Parameters")
    crossover_rate = st.sidebar.slider("Crossover Rate (CO_R)", 0.0, 0.95, 0.8)
    mutation_rate = st.sidebar.slider("Mutation Rate (MUT_R)", 0.01, 0.05, 0.02)
    
    if st.button("Run Genetic Algorithm"):
        schedule = run_ga(data, crossover_rate, mutation_rate)
        st.subheader("Generated TV Schedule")
        st.dataframe(schedule)
