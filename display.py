import streamlit as st
import pandas as pd
from logics import Dataset

def display_overall_df(dataset_instance):
    st.subheader("DataFrame")
    
    summary_df = dataset_instance.get_summary()
    st.table(summary_df)

    st.subheader("Columns")
    if dataset_instance.table is not None:
        st.table(dataset_instance.table) 

    with st.expander("Explore Dataframe"):
        n_rows = st.slider("Select the number of rows to be displayed", min_value=5, max_value=50, value=5)

        view_method = st.radio("Exploration Method", options=["Head", "Tail", "Sample"])
        if view_method == "Head":
            subset = dataset_instance.get_head(n_rows)
        elif view_method == "Tail":
            subset = dataset_instance.get_tail(n_rows)
        else:
            subset = dataset_instance.get_sample(n_rows)
        st.write("Top Rows of Selected Table")
        st.dataframe(subset)
def main():
    st.title("CSV Explorer")
    st.subheader("Choose a CSV file")

    uploaded_file = st.file_uploader("Drag and drop file here", type=["csv"])
    if uploaded_file is not None:
        dataset_instance = Dataset(uploaded_file)
        dataset_instance.set_data()  
        display_overall_df(dataset_instance)
    else:
        st.info("Please upload a CSV file to explore.")

if __name__ == "__main__":
    main()