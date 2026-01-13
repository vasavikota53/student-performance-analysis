import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("📊 Student Performance Data Analysis")
st.write(
    """
    This project analyzes student performance data.
    It helps understand how scores vary based on different factors.
    """
)


# Load dataset
df = pd.read_csv("data/StudentsPerformance.csv")

# Feature engineering
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

# Show data
st.subheader("Dataset Preview")
st.write("This table shows the first 5 rows of our student performance dataset. You can see scores in math, reading, and writing.")
st.dataframe(df.head())

st.write("click the below checkbox if you want to see the full dataset")
if st.checkbox("Show full dataset"):
    st.dataframe(df)


# Gender filter
st.subheader("select gender that you want to perform data analysis of students")
gender = st.selectbox("Select Gender", ["All"] + list(df['gender'].unique()))

if gender != "All":
    df = df[df['gender'] == gender]


min_score = st.slider(
    "**select the minimum avg score of students that you want to start analysis from**",
    min_value=0,
    max_value=100,
    value=50
)

df = df[df['average_score'] >= min_score]
st.dataframe(df)



# Plot
st.subheader("Average Score Distribution")
fig, ax = plt.subplots()
sns.histplot(df['average_score'], bins=10, kde=True, ax=ax)
st.pyplot(fig)

st.success("Analysis completed.")



