import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

    

@st.cache_data
def load_data():
    return pd.read_csv("csv/titanic_data.csv")

data = load_data()

st.sidebar.title("🚢 Titanic Data Analysis")
section = st.sidebar.radio("Go to", ["Home", "Data Cleaning", "Exploratory Analysis", "Feature Engineering", "Insights"])

if section == "Home":
    st.title("Titanic Dataset Exploratory Data Analysis")
    st.write("Performing an in-depth analysis of the Titanic dataset.")
    st.subheader("Dataset Preview")
    st.dataframe(data.head())

if section == "Data Cleaning":
    st.title("🛠 Data Cleaning")

    st.subheader("Missing Values")
    missing_data = data.isnull().sum()
    st.write(missing_data)

    if st.button("Fill missing Age with median"):
        data["Age"].fillna(data["Age"].median(), inplace=True)
        st.success("Filled missing Age values with median!")

    if st.button("Fill missing Embarked with mode"):
        data["Embarked"].fillna(data["Embarked"].mode()[0], inplace=True)
        st.success("Filled missing Embarked values with mode!")

    if st.button("Drop duplicates"):
        data.drop_duplicates(inplace=True)
        st.success("Removed duplicate entries!")

    st.subheader("Cleaned Dataset Preview")
    st.dataframe(data.head())

# (EDA) Section
if section == "Exploratory Analysis":
    st.title("📊 Exploratory Data Analysis")

    # Statistical Summary
    st.subheader("Statistical Summary")
    st.write(data.describe())

    # Age Distribution
    st.subheader("Age Distribution")
    fig, ax = plt.subplots()
    sns.histplot(data["Age"].dropna(), kde=True, ax=ax)
    ax.set_title("Age Distribution")
    st.pyplot(fig)

    # Gender Distribution
    st.subheader("Gender Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x="Sex", data=data, ax=ax)
    ax.set_title("Gender Distribution")
    st.pyplot(fig)

    # Survival Rate by Gender
    st.subheader("Survival Rate by Gender")
    fig, ax = plt.subplots()
    sns.barplot(x="Sex", y="Survived", data=data, ax=ax)
    ax.set_title("Survival Rate by Gender")
    st.pyplot(fig)

    # Pclass vs Survived
    st.subheader("Pclass vs Survived")
    fig, ax = plt.subplots()
    sns.countplot(x="Pclass", hue="Survived", data=data, ax=ax)
    ax.set_title("Pclass vs Survived")
    st.pyplot(fig)

    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Heatmap")
    st.pyplot(fig)

if section == "Feature Engineering":
    st.title("⚙️ Feature Engineering")

    st.subheader("Creating Family Size Feature")
    data["FamilySize"] = data["SibSp"] + data["Parch"] + 1  # Include self
    fig, ax = plt.subplots()
    sns.histplot(data["FamilySize"], kde=True, ax=ax)
    ax.set_title("Family Size Distribution")
    st.pyplot(fig)

    st.write("New Feature: **FamilySize = SibSp + Parch + 1**")
    st.dataframe(data[["SibSp", "Parch", "FamilySize"]].head())

if section == "Insights":
    st.title("📌 Key Insights")
    insights = """
    - **Females had a higher survival rate than males.**
    - **1st-class passengers had the highest survival rate.**
    - **The majority of passengers belonged to Pclass 3.**
    - **Younger passengers tended to survive more often.**
    - **Having a larger family size impacted survival rates.**
    """
    st.write(insights)



# conditional statements
santhu = 4+5
if False:
   print("Data science")
elif (santhu):
    print("the value is",santhu)
else:
    print("hmm")
    
san = 7
k = 5

if (san) > (k):
    print("the small value is", san+k) 
elif (k) < (san):
   print("the great value is", k-san)
else:
    print("Not found!)
    

