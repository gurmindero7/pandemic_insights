# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Title of the Streamlit app
# st.title("COVID-19 Data Visualization")

# # Load datasets
# dataset1 = pd.read_csv("covid.csv")
# dataset2 = pd.read_csv("covid_grouped.csv")

# # Drop columns
# dataset1.drop(['NewCases', 'NewDeaths', 'NewRecovered'], axis=1, inplace=True)

# # Plotly visualizations
# fig1 = px.bar(dataset1.head(15), x='Country/Region', y='TotalCases', color='TotalCases', height=500, hover_data=['Country/Region', 'Continent'])
# st.plotly_chart(fig1)

# fig2 = px.bar(dataset1.head(15), x='Country/Region', y='TotalCases', color='TotalDeaths', height=500, hover_data=['Country/Region', 'Continent'])
# st.plotly_chart(fig2)

# fig3 = px.bar(dataset1.head(15), x='TotalTests', y='Country/Region', color='TotalTests', orientation='h', height=500, hover_data=['Country/Region', 'Continent'])
# st.plotly_chart(fig3)

# fig4 = px.bar(dataset1.head(15), x='TotalTests', y='Continent', color='TotalTests', orientation='h', height=500, hover_data=['Country/Region', 'Continent'])
# st.plotly_chart(fig4)

# fig5 = px.scatter(dataset1, x='Continent', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='TotalCases', size='TotalCases', size_max=80)
# st.plotly_chart(fig5)

# fig6 = px.scatter(dataset1.head(57), x='Continent', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='TotalCases', size='TotalCases', size_max=80, log_y=True)
# st.plotly_chart(fig6)

# fig7 = px.scatter(dataset1.head(54), x='Continent', y='TotalTests', hover_data=['Country/Region', 'Continent'], color='TotalTests', size='TotalTests', size_max=80)
# st.plotly_chart(fig7)

# fig8 = px.scatter(dataset1.head(50), x='Continent', y='TotalTests', hover_data=['Country/Region', 'Continent'], color='TotalTests', size='TotalTests', size_max=80, log_y=True)
# st.plotly_chart(fig8)

# fig9 = px.scatter(dataset1.head(100), x='Country/Region', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='TotalCases', size='TotalCases', size_max=80)
# st.plotly_chart(fig9)

# fig10 = px.scatter(dataset1.head(30), x='Country/Region', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalCases', size_max=80, log_y=True)
# st.plotly_chart(fig10)

# fig11 = px.scatter(dataset1.head(10), x='Country/Region', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalDeaths', size_max=80)
# st.plotly_chart(fig11)

# fig12 = px.scatter(dataset1.head(30), x='Country/Region', y='Tests/1M pop', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='Tests/1M pop', size_max=80)
# st.plotly_chart(fig12)

# fig13 = px.scatter(dataset1.head(30), x='Country/Region', y='Tests/1M pop', hover_data=['Country/Region', 'Continent'], color='Tests/1M pop', size='Tests/1M pop', size_max=80)
# st.plotly_chart(fig13)

# fig14 = px.scatter(dataset1.head(30), x='TotalCases', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='TotalDeaths', size='TotalDeaths', size_max=80)
# st.plotly_chart(fig14)

# fig15 = px.scatter(dataset1.head(30), x='TotalCases', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='TotalDeaths', size='TotalDeaths', size_max=80, log_x=True, log_y=True)
# st.plotly_chart(fig15)

# fig16 = px.bar(dataset2, x="Date", y="Confirmed", color="Confirmed", hover_data=["Confirmed", "Date", "Country/Region"], height=400)
# st.plotly_chart(fig16)

# fig17 = px.bar(dataset2, x="Date", y="Confirmed", color="Confirmed", hover_data=["Confirmed", "Date", "Country/Region"], log_y=True, height=400)
# st.plotly_chart(fig17)

# fig18 = px.bar(dataset2, x="Date", y="Deaths", color="Deaths", hover_data=["Confirmed", "Date", "Country/Region"], log_y=False, height=400)
# st.plotly_chart(fig18)

# df_US = dataset2.loc[dataset2["Country/Region"] == "US"]

# fig19 = px.bar(df_US, x="Date", y="Confirmed", color="Confirmed", height=400)
# st.plotly_chart(fig19)

# fig20 = px.bar(df_US, x="Date", y="Recovered", color="Recovered", height=400)
# st.plotly_chart(fig20)

# fig21 = px.line(df_US, x="Date", y="Recovered", height=400)
# st.plotly_chart(fig21)

# fig22 = px.line(df_US, x="Date", y="Deaths", height=400)
# st.plotly_chart(fig22)

# fig23 = px.line(df_US, x="Date", y="Confirmed", height=400)
# st.plotly_chart(fig23)

# fig24 = px.line(df_US, x="Date", y="New cases", height=400)
# st.plotly_chart(fig24)

# fig25 = px.bar(df_US, x="Date", y="New cases", height=400)
# st.plotly_chart(fig25)

# fig26 = px.scatter(df_US, x="Confirmed", y="Deaths", height=400)
# st.plotly_chart(fig26)

# fig27 = px.choropleth(dataset2, locations="iso_alpha", color="Confirmed", hover_name="Country/Region", color_continuous_scale="Blues", animation_frame="Date")
# st.plotly_chart(fig27)

# import streamlit as st
# import pandas as pd
# import plotly.express as px


# # Title of the Streamlit app
# st.title("COVID-19 Data Visualization")

# # Load datasets
# dataset1 = pd.read_csv("covid.csv")
# dataset2 = pd.read_csv("covid_grouped.csv")

# # Drop columns
# dataset1.drop(['NewCases', 'NewDeaths', 'NewRecovered'], axis=1, inplace=True)

# # Define discrete color sequences
# discrete_colors = px.colors.qualitative.Plotly

# # Plotly visualizations
# fig1 = px.bar(dataset1.head(15), x='Country/Region', y='TotalCases', color='Country/Region', height=500, hover_data=['Country/Region', 'Continent'], color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig1)

# fig2 = px.bar(dataset1.head(15), x='Country/Region', y='TotalCases', color='Country/Region', height=500, hover_data=['Country/Region', 'Continent'], color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig2)

# fig3 = px.bar(dataset1.head(15), x='TotalTests', y='Country/Region', color='Country/Region', orientation='h', height=500, hover_data=['Country/Region', 'Continent'], color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig3)

# fig4 = px.bar(dataset1.head(15), x='TotalTests', y='Continent', color='Continent', orientation='h', height=500, hover_data=['Country/Region', 'Continent'], color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig4)

# fig5 = px.scatter(dataset1, x='Continent', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='Continent', size='TotalCases', size_max=80, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig5)

# fig6 = px.scatter(dataset1.head(57), x='Continent', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='Continent', size='TotalCases', size_max=80, log_y=True, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig6)

# fig7 = px.scatter(dataset1.head(54), x='Continent', y='TotalTests', hover_data=['Country/Region', 'Continent'], color='Continent', size='TotalTests', size_max=80, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig7)

# fig8 = px.scatter(dataset1.head(50), x='Continent', y='TotalTests', hover_data=['Country/Region', 'Continent'], color='Continent', size='TotalTests', size_max=80, log_y=True, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig8)

# fig9 = px.scatter(dataset1.head(100), x='Country/Region', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalCases', size_max=80, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig9)

# fig10 = px.scatter(dataset1.head(30), x='Country/Region', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalCases', size_max=80, log_y=True, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig10)

# fig11 = px.scatter(dataset1.head(10), x='Country/Region', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalDeaths', size_max=80, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig11)

# fig12 = px.scatter(dataset1.head(30), x='Country/Region', y='Tests/1M pop', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='Tests/1M pop', size_max=80, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig12)

# fig13 = px.scatter(dataset1.head(30), x='Country/Region', y='Tests/1M pop', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='Tests/1M pop', size_max=80, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig13)

# fig14 = px.scatter(dataset1.head(30), x='TotalCases', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalDeaths', size_max=80, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig14)

# fig15 = px.scatter(dataset1.head(30), x='TotalCases', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalDeaths', size_max=80, log_x=True, log_y=True, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig15)

# fig16 = px.bar(dataset2, x="Date", y="Confirmed", color="Country/Region", hover_data=["Confirmed", "Date", "Country/Region"], height=400, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig16)

# fig17 = px.bar(dataset2, x="Date", y="Confirmed", color="Country/Region", hover_data=["Confirmed", "Date", "Country/Region"], log_y=True, height=400, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig17)

# fig18 = px.bar(dataset2, x="Date", y="Deaths", color="Country/Region", hover_data=["Confirmed", "Date", "Country/Region"], log_y=False, height=400, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig18)

# df_US = dataset2.loc[dataset2["Country/Region"] == "US"]

# fig19 = px.bar(df_US, x="Date", y="Confirmed", color="Confirmed", height=400, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig19)

# fig20 = px.bar(df_US, x="Date", y="Recovered", color="Recovered", height=400, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig20)

# fig21 = px.line(df_US, x="Date", y="Recovered", height=400, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig21)

# fig22 = px.line(df_US, x="Date", y="Deaths", height=400, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig22)

# fig23 = px.line(df_US, x="Date", y="Confirmed", height=400, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig23)

# fig24 = px.line(df_US, x="Date", y="New cases", height=400, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig24)

# fig25 = px.bar(df_US, x="Date", y="New cases", height=400, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig25)

# fig26 = px.scatter(df_US, x="Confirmed", y="Deaths", height=400, color_discrete_sequence=discrete_colors)
# st.plotly_chart(fig26)

# fig27 = px.choropleth(dataset2, locations="iso_alpha", color="Confirmed", hover_name="Country/Region", color_continuous_scale="Blues", animation_frame="Date")
# st.plotly_chart(fig27)

# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Title of the Streamlit app
# st.title("COVID-19 Data Visualization")

# # Load datasets
# dataset1 = pd.read_csv("covid.csv")
# dataset2 = pd.read_csv("covid_grouped.csv")

# # Drop columns
# dataset1.drop(['NewCases', 'NewDeaths', 'NewRecovered'], axis=1, inplace=True)

# # Plotly visualizations
# fig1 = px.bar(dataset1.head(15), x='Country/Region', y='TotalCases', color='Country/Region', height=500, hover_data=['Country/Region', 'Continent'], color_discrete_sequence=px.colors.qualitative.G10)
# st.plotly_chart(fig1)

# fig2 = px.bar(dataset1.head(15), x='Country/Region', y='TotalCases', color='TotalDeaths', height=500, hover_data=['Country/Region', 'Continent'], color_discrete_sequence=px.colors.qualitative.Dark2)
# st.plotly_chart(fig2)

# fig3 = px.bar(dataset1.head(15), x='TotalTests', y='Country/Region', color='TotalTests', orientation='h', height=500, hover_data=['Country/Region', 'Continent'], color_discrete_sequence=px.colors.qualitative.Alphabet)
# st.plotly_chart(fig3)

# fig4 = px.bar(dataset1.head(15), x='TotalTests', y='Continent', color='Continent', orientation='h', height=500, hover_data=['Country/Region', 'Continent'], color_discrete_sequence=px.colors.qualitative.Dark24)

# fig5 = px.scatter(dataset1, x='Continent', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='Continent', size='TotalCases', size_max=80, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig5)

# fig6 = px.scatter(dataset1.head(57), x='Continent', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='Continent', size='TotalCases', size_max=80, log_y=True, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig6)

# fig7 = px.scatter(dataset1.head(54), x='Continent', y='TotalTests', hover_data=['Country/Region', 'Continent'], color='Continent', size='TotalTests', size_max=80, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig7)

# fig8 = px.scatter(dataset1.head(50), x='Continent', y='TotalTests', hover_data=['Country/Region', 'Continent'], color='Continent', size='TotalTests', size_max=80, log_y=True, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig8)

# fig9 = px.scatter(dataset1.head(100), x='Country/Region', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalCases', size_max=80, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig9)

# fig10 = px.scatter(dataset1.head(30), x='Country/Region', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalCases', size_max=80, log_y=True, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig10)

# fig11 = px.scatter(dataset1.head(10), x='Country/Region', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalDeaths', size_max=80, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig11)

# fig12 = px.scatter(dataset1.head(30), x='Country/Region', y='Tests/1M pop', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='Tests/1M pop', size_max=80, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig12)

# fig13 = px.scatter(dataset1.head(30), x='Country/Region', y='Tests/1M pop', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='Tests/1M pop', size_max=80, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig13)

# fig14 = px.scatter(dataset1.head(30), x='TotalCases', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalDeaths', size_max=80, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig14)

# fig15 = px.scatter(dataset1.head(30), x='TotalCases', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalDeaths', size_max=80, log_x=True, log_y=True, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig15)

# fig16 = px.bar(dataset2, x="Date", y="Confirmed", color="Country/Region", hover_data=["Confirmed", "Date", "Country/Region"], height=400, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig16)

# fig17 = px.bar(dataset2, x="Date", y="Confirmed", color="Country/Region", hover_data=["Confirmed", "Date", "Country/Region"], log_y=True, height=400, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig17)

# fig18 = px.bar(dataset2, x="Date", y="Deaths", color="Country/Region", hover_data=["Confirmed", "Date", "Country/Region"], log_y=False, height=400, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig18)

# df_US = dataset2.loc[dataset2["Country/Region"] == "US"]

# fig19 = px.bar(df_US, x="Date", y="Confirmed", color="Confirmed", height=400, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig19)

# fig20 = px.bar(df_US, x="Date", y="Recovered", color="Recovered", height=400, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig20)

# fig21 = px.line(df_US, x="Date", y="Recovered", height=400, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig21)

# fig22 = px.line(df_US, x="Date", y="Deaths", height=400, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig22)

# fig23 = px.line(df_US, x="Date", y="Confirmed", height=400, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig23)

# fig24 = px.line(df_US, x="Date", y="New cases", height=400, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig24)

# fig25 = px.bar(df_US, x="Date", y="New cases", height=400, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig25)

# fig26 = px.scatter(df_US, x="Confirmed", y="Deaths", height=400, color_discrete_sequence=px.colors.qualitative.Dark24)
# st.plotly_chart(fig26)

# fig27 = px.choropleth(dataset2, locations="iso_alpha", color="Confirmed", hover_name="Country/Region", color_continuous_scale="Blues", animation_frame="Date")
# st.plotly_chart(fig27)

# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Title of the Streamlit app
# st.title("COVID-19 Data Visualization")

# # Load datasets
# dataset1 = pd.read_csv("covid.csv")
# dataset2 = pd.read_csv("covid_grouped.csv")

# # Drop columns
# dataset1.drop(['NewCases', 'NewDeaths', 'NewRecovered'], axis=1, inplace=True)

# # Plotly visualizations

# fig1 = px.bar(dataset1.head(15), x='Country/Region', y='TotalCases', color='TotalDeaths', height=500, hover_data=['Country/Region', 'Continent'], color_continuous_scale='Plasma')
# st.plotly_chart(fig1)

# fig2 = px.scatter(dataset1, x='Continent', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='TotalCases', size='TotalCases', size_max=80, color_continuous_scale='Viridis')
# st.plotly_chart(fig2)

# fig3 = px.scatter(dataset1.head(50), x='Continent', y='TotalTests', hover_data=['Country/Region', 'Continent'], color='TotalTests', size='TotalTests', size_max=80, log_y=True, color_continuous_scale='Plasma')
# st.plotly_chart(fig3)

# fig4 = px.scatter(dataset1.head(30), x='Country/Region', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='TotalCases', size='TotalCases', size_max=80, log_y=True, color_continuous_scale='Plasma')
# st.plotly_chart(fig4)

# fig5 = px.scatter(dataset1.head(10), x='Country/Region', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='TotalDeaths', size='TotalDeaths', size_max=80, color_continuous_scale='Viridis')
# st.plotly_chart(fig5)

# fig6 = px.scatter(dataset1.head(30), x='Country/Region', y='Tests/1M pop', hover_data=['Country/Region', 'Continent'], color='Tests/1M pop', size='Tests/1M pop', size_max=80, color_continuous_scale='Plasma')
# st.plotly_chart(fig6)

# fig7 = px.scatter(dataset1.head(30), x='TotalCases', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='TotalDeaths', size='TotalDeaths', size_max=80, log_x=True, log_y=True, color_continuous_scale='Viridis')
# st.plotly_chart(fig7)

# df_US = dataset2.loc[dataset2["Country/Region"] == "US"]

# fig8 = px.choropleth(dataset2, locations="iso_alpha", color="Confirmed", hover_name="Country/Region", color_continuous_scale="Viridis", animation_frame="Date")
# st.plotly_chart(fig8)

import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the Streamlit app
st.title("COVID-19 Data Visualization")

# Load datasets
dataset1 = pd.read_csv("covid.csv")
dataset2 = pd.read_csv("covid_grouped.csv")

# Drop columns
dataset1.drop(['NewCases', 'NewDeaths', 'NewRecovered'], axis=1, inplace=True)

# Sidebar menu for visualizations
option = st.sidebar.selectbox(
    'Select a visualization',
    [
        'Bar Chart: Total Cases by Country',
        'Scatter Plot: Total Cases by Continent',
        'Scatter Plot: Total Tests by Continent (Log Scale)',
        'Scatter Plot: Total Cases by Country (Log Scale)',
        'Scatter Plot: Total Deaths by Country',
        'Scatter Plot: Tests per 1M pop by Country',
        'Scatter Plot: Total Cases vs Total Deaths (Log Scale)',
        'Choropleth Map: Confirmed Cases'
    ]
)

# Display the selected visualization
if option == 'Bar Chart: Total Cases by Country':
    fig1 = px.bar(dataset1.head(15), x='Country/Region', y='TotalCases', color='TotalDeaths', height=500, hover_data=['Country/Region', 'Continent'], color_continuous_scale='Plasma')
    st.plotly_chart(fig1)

elif option == 'Scatter Plot: Total Cases by Continent':
    fig2 = px.scatter(dataset1, x='Continent', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='TotalCases', size='TotalCases', size_max=80, color_continuous_scale='Viridis')
    st.plotly_chart(fig2)

elif option == 'Scatter Plot: Total Tests by Continent (Log Scale)':
    fig3 = px.scatter(dataset1.head(50), x='Continent', y='TotalTests', hover_data=['Country/Region', 'Continent'], color='TotalTests', size='TotalTests', size_max=80, log_y=True, color_continuous_scale='Plasma')
    st.plotly_chart(fig3)

elif option == 'Scatter Plot: Total Cases by Country (Log Scale)':
    fig4 = px.scatter(dataset1.head(30), x='Country/Region', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='TotalCases', size='TotalCases', size_max=80, log_y=True, color_continuous_scale='Plasma')
    st.plotly_chart(fig4)

elif option == 'Scatter Plot: Total Deaths by Country':
    fig5 = px.scatter(dataset1.head(10), x='Country/Region', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='TotalDeaths', size='TotalDeaths', size_max=80, color_continuous_scale='Viridis')
    st.plotly_chart(fig5)

elif option == 'Scatter Plot: Tests per 1M pop by Country':
    fig6 = px.scatter(dataset1.head(30), x='Country/Region', y='Tests/1M pop', hover_data=['Country/Region', 'Continent'], color='Tests/1M pop', size='Tests/1M pop', size_max=80, color_continuous_scale='Plasma')
    st.plotly_chart(fig6)

elif option == 'Scatter Plot: Total Cases vs Total Deaths (Log Scale)':
    fig7 = px.scatter(dataset1.head(30), x='TotalCases', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='TotalDeaths', size='TotalDeaths', size_max=80, log_x=True, log_y=True, color_continuous_scale='Viridis')
    st.plotly_chart(fig7)

elif option == 'Choropleth Map: Confirmed Cases':
    fig8 = px.choropleth(dataset2, locations="iso_alpha", color="Confirmed", hover_name="Country/Region", color_continuous_scale="Viridis", animation_frame="Date")
    st.plotly_chart(fig8)
