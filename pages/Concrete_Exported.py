import streamlit as st
import pandas as pd

# load data from excel sheet
df = pd.read_excel("تسجيل صادر خرسانة محطة ابو حمص.xlsx", sheet_name='صادر خرسانة', skiprows=3, engine='openpyxl')
st.set_page_config(layout='wide')

column_names = df.columns.tolist()

# Create the Streamlit app
st.title('صادرات محطة الخرسانة - أبو حمص')

# Add a dropdown widget to select the column
selected_column = st.selectbox('Select a column:', column_names)

# Filter the data based on the selected column
filtered_data = df[selected_column].dropna().unique().tolist()

# Add a dropdown widget to select the filtered item
selected_item = st.selectbox('Select an item:', filtered_data)

# Filter the dataframe based on the selected item
filtered_df = df[df[selected_column] == selected_item]

# Calculate the sum of "الكميه" column for each element of "اسم الخامة" and round to two decimal places
sum_by_material = filtered_df.groupby('اسم الخامة')['الكمية'].sum().round(2).reset_index()

# Format the values without trailing zeros
sum_by_material['الكمية'] = sum_by_material['الكمية'].map('{:.2f}'.format)

# Format the table display
sum_by_material_styled = sum_by_material.style.set_properties(**{'text-align': 'center'}).\
    set_table_styles([{
        'selector': 'th',
        'props': [('text-align', 'center')]
    }]).\
    set_properties(subset=['الكمية'], **{'text-align': 'center'})

# Display the filtered dataframe
st.write('Filtered Data:')
st.write(filtered_df)

# Display the sum of "الكميه" column for each element of "اسم الخامة"
st.write('Sum of الكمية column by material:')
st.dataframe(sum_by_material_styled, height=200)