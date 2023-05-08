import streamlit as st
import pandas as pd

# Load data from Excel sheet
df = pd.read_excel("تسجيل صادر خرسانة محطة ابو حمص.xlsx", sheet_name='صادر خرسانة', skiprows=3, engine='openpyxl')
st.set_page_config(layout='wide')

column_names = df.columns.tolist()

# Create the Streamlit app
st.title('صادرات محطة الخرسانة - أبو حمص')

# Add dropdown widgets to select the columns for filtering
filter_columns = st.multiselect('Select columns for filtering:', column_names)

# Apply filters to the DataFrame
filtered_df = df.copy()
for col in filter_columns:
    selected_values = st.multiselect(f'Select {col}:', df[col].dropna().unique().tolist())
    filtered_df = filtered_df[filtered_df[col].isin(selected_values)]

# Calculate the sum of "الكمية" column for each element of "اسم الخامة" and round to two decimal places
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

# Display the sum of "الكمية" column for each element of "اسم الخامة"
st.write('Sum of الكمية column by material:')
st.dataframe(sum_by_material_styled, height=200)
