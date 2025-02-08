import streamlit as st 
import pandas as pd 

#Define the Main Page Including Title and Introduction
def main(): 
    # Title 
    st.title("Palmer's Penguins Data Explorer!")
    # Description
    st.write("**This app allows you to explore the Palmer's Penguins dataset with interactive filtering options. This page displays data and interactivity options for Palmer's Penguins. You can filter the penguins by *species*, *island*, and *flipper length*.**")
    st.write("**Have fun!!**")
    st.markdown("---")

if __name__ == "__main__":
    main()


# Load Penguin Dataset
@st.cache_data
def load_data():
    penguin = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
    return pd.read_csv(penguin)

# Load DataFrame
df = load_data()
st.write("Here's the dataset loaded from a CSV file:") 
st.dataframe(df)

# Interactive Filter #1: Penguin Species 
species = st.selectbox("**Select Species:**", df["species"].unique())
filtered_df = df[df["species"] == species]

# Display the Results of Filter #1
st.write(f"### Penguins of {species} Species:")
st.dataframe(filtered_df)

# Interactive Filter #2: Penguin Island
island = st.selectbox("**Select Island:**", df["island"].unique())
filtered_df = filtered_df[filtered_df["island"] == island]

# Display the Results of Filter #2: 
st.write(f"### Penguins from {island} Island:")
st.dataframe(filtered_df)

# Interactive Filter #3: Penguin Flipper Length 
flipper_min, flipper_max = st.slider("**Filter by Flipper Length (mm):**", int(df["flipper_length_mm"].min()), int(df["flipper_length_mm"].max()), (int(df["flipper_length_mm"].min()), int(df["flipper_length_mm"].max())))
filtered_df = filtered_df[(filtered_df["flipper_length_mm"] >= flipper_min) & (filtered_df["flipper_length_mm"] <= flipper_max)]

#Display the Results of Filter #3: 
st.write(f"### Penguins with Flipper Length Between {flipper_min} mm and {flipper_max} mm:")
st.dataframe(filtered_df)