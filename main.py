import streamlit as st
import matplotlib.pyplot as plt
from data_utils import load_data, search_by_name, filter_by_gender, people_in_age_range

data = load_data('thimmayapalli.csv')

# Streamlit user interface
st.title('Data Search and Filter Application')
st.title("Thimmayepalle")

# Display total voters and gender count
total_voters = len(data)
male_count = len(data[data['Gender'].str.lower() == 'male'])
female_count = len(data[data['Gender'].str.lower() == 'female'])

# Display total voters and gender count
total_voters = len(data)
st.write(f"Total Voters: {total_voters}")

# Pie chart for gender distribution
fig, ax = plt.subplots()
ax.pie([male_count, female_count], labels=['Male', 'Female'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)

# Name search
st.subheader('Search by Name')
name_query = st.text_input("Enter the name to search:")
if st.button('Search Name', key='name_search'):
    name_results, name_count = search_by_name(data,name_query)
    st.write(name_results)
    if name_count > 0:
        name_percentage = (name_count / total_voters) * 100
        st.write(f"Number of people with name '{name_query}': {name_count}")
        st.write(f"Percentage of total: {name_percentage:.2f}%")
        
        # Pie chart for name search distribution
        fig, ax = plt.subplots()
        ax.pie([name_count, total_voters - name_count], labels=[name_query, 'Others'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)

# Gender filter
st.subheader('Filter by Gender')
gender = st.selectbox('Select Gender:', ['Male', 'Female'], key='gender_select')
if st.button('Filter Gender', key='gender_filter'):
    gender_results = filter_by_gender(data,gender)
    st.write(gender_results)

# Age filter
st.subheader('People within a specified age range')
min_age, max_age = st.slider('Select age range:', 0, 100, (20, 25))
if st.button('Show People Within Age Range', key='age_range'):
    age_results, age_count = people_in_age_range(data, min_age, max_age)
    st.write(age_results)
    if age_count > 0:
        age_percentage = (age_count / total_voters) * 100
        st.write(f"Number of people aged {min_age} to {max_age}: {age_count}")
        st.write(f"Percentage of total: {age_percentage:.2f}%")
        
        # Pie chart for age range distribution
        fig, ax = plt.subplots()
        ax.pie([age_count, total_voters - age_count], labels=[f'{min_age}-{max_age}', 'Others'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)
