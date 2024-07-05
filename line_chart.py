# import pandas as pd
# import streamlit as st
# import matplotlib.pyplot as plt
# df = pd.read_csv('day_wise.csv')
# st.title("COVID-19 Data Visualization")

# # Set the date column as the index
# df['Date'] = pd.to_datetime(df['Date'])
# df = df.set_index('Date')

# # Create the line chart
# fig, ax = plt.subplots(figsize=(12, 6))
# ax.plot(df.index, df['Confirmed'], label='Confirmed')
# ax.plot(df.index, df['Deaths'], label='Deaths')
# ax.plot(df.index, df['Recovered'], label='Recovered')
# ax.plot(df.index, df['Active'], label='Active')
# ax.plot(df.index, df['New cases'], label='New cases')
# ax.plot(df.index, df['New deaths'], label='New deaths')
# ax.plot(df.index, df['New recovered'], label='New recovered')

# # Set the x-axis tick labels to the date
# ax.set_xticks(df.index[::30])
# ax.set_xticklabels(df.index.strftime('%Y-%m-%d')[::30], rotation=45)

# # Add labels and legend
# ax.set_xlabel('Date')
# ax.set_ylabel('Number')
# ax.legend()

# st.plotly_chart(fig)
# # Calculate additional metrics
# df['Deaths / 100 Cases'] = (df['Deaths'] / df['Confirmed']) * 100
# df['Recovered / 100 Cases'] = (df['Recovered'] / df['Confirmed']) * 100
# df['Deaths / 100 Recovered'] = (df['Deaths'] / df['Recovered']) * 100
# df['No. of countries'] = df['Confirmed'].count()

# # Display the additional metrics
# st.subheader("Additional Metrics")
# st.write(df[['Deaths / 100 Cases', 'Recovered / 100 Cases', 'Deaths / 100 Recovered', 'No. of countries']])



import pandas as pd
import streamlit as st
import plotly.graph_objects as go

df = pd.read_csv('day_wise.csv')
st.title("COVID-19 Data Visualization")

# Set the date column as the index
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# Create the line chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['Confirmed'], mode='lines', name='Confirmed'))
fig.add_trace(go.Scatter(x=df.index, y=df['Deaths'], mode='lines', name='Deaths'))
fig.add_trace(go.Scatter(x=df.index, y=df['Recovered'], mode='lines', name='Recovered'))
fig.add_trace(go.Scatter(x=df.index, y=df['Active'], mode='lines', name='Active'))
fig.add_trace(go.Scatter(x=df.index, y=df['New cases'], mode='lines', name='New cases'))
fig.add_trace(go.Scatter(x=df.index, y=df['New deaths'], mode='lines', name='New deaths'))
fig.add_trace(go.Scatter(x=df.index, y=df['New recovered'], mode='lines', name='New recovered'))

# Set the x-axis tick labels to the date
fig.update_layout(
    xaxis_tickmode='array',
    xaxis_tickvals=df.index[::30],
    xaxis_ticktext=df.index.strftime('%Y-%m-%d')[::30],
    xaxis_tickangle=45,
    xaxis_title='Date',
    yaxis_title='Number',
    title='COVID-19 Data Visualization',
    legend_title='Metrics',
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="RebeccaPurple"
    )
)

st.plotly_chart(fig, use_container_width=True)

# Add additional metrics
st.subheader("Additional Metrics")
st.write(df[['Deaths / 100 Cases', 'Recovered / 100 Cases', 'Deaths / 100 Recovered', 'No. of countries']])