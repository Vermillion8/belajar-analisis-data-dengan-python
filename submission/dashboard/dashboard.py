import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

merged_hour = pd.read_csv('./dashboard/merged_hour.csv')
merged_month = pd.read_csv('./dashboard/merged_month.csv')
merged_year = pd.read_csv('./dashboard/merged_year.csv')

def correlationPlot():
  merged_hour.replace(1, np.nan, inplace=True) # Replace 1 with NaN
  merged_hour_flat = pd.Series(merged_hour.values.ravel()).drop_duplicates()
  merged_hour_flat = merged_hour_flat[merged_hour_flat.apply(lambda x: isinstance(x, float))]
  
  merged_month.replace(1, np.nan, inplace=True) # Replace 1 with NaN
  merged_month_flat = pd.Series(merged_month.values.ravel()).drop_duplicates()
  merged_month_flat = merged_month_flat[merged_month_flat.apply(lambda x: isinstance(x, float))]
  
  merged_year.replace(1, np.nan, inplace=True) # Replace 1 with NaN
  merged_year_flat = pd.Series(merged_year.values.ravel()).drop_duplicates()
  merged_year_flat = merged_year_flat[merged_year_flat.apply(lambda x: isinstance(x, float))]
  
  # st.write(merged_hour_flat)

  categories = ['PM2.5 & PM10', 'SO2 & NO2', 'CO & O3']
  values = [merged_hour_flat.mean(), merged_month_flat.mean(), merged_year_flat.mean()]
  colors = ['red', 'green', 'blue']

  fig, ax = plt.subplots()
  ax.bar(categories, values, color=colors)
  ax.set_ylim(-1, 1)
  ax.set_xlabel('Categories')
  ax.set_ylabel('Mean Correlation')
  ax.set_title('Mean Correlation of Different Categories')
  st.pyplot(fig)
  
def main():
  
  st.title("Data Dashboard")
  
  # Add a sidebar for user input
  st.sidebar.title("User Input")

  # Add a selectbox for choosing the data to display
  data_choice = st.sidebar.selectbox("Choose Data", ["PM2.5 & PM10", "SO2 & NO2", "CO & O3", "Correlation Plot"])

  # Display the selected data based on user input
  if data_choice == "PM2.5 & PM10":
    st.subheader("Particle Matter Correlation Data")
    st.dataframe(merged_hour)
  elif data_choice == "SO2 & NO2":
    st.subheader("Gaseous Matter Correlation Data")
    st.dataframe(merged_month)
  elif data_choice == "CO & O3":
    st.subheader("Gaseous Matter Correlation Data")
    st.dataframe(merged_year)
  elif data_choice == "Correlation Plot":
    st.subheader("Correlation Plot")
    correlationPlot()


if __name__ == '__main__':
  main()