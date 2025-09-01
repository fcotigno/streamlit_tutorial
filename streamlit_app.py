import streamlit as st
import pandas as pd
import plotly.express as px

# (Optional) cache for faster reloads
@st.cache_data
def load_data():
    return pd.read_csv("state_data.csv")

df = load_data()

st.header("Changes in US State Demographics Over Time")

# Selections
state = st.selectbox("Select a state:", df["State"].unique(), key="state")
demographic = st.selectbox(
    "Select a demographic:",
    ["Total Population", "Median Household Income"],
    key="demographic"
)

# Filter once, reuse
df_state = df[df["State"] == state]

# ---- Tabs ----
tab_graphs, tab_table = st.tabs(["Graphs", "Table"])

with tab_graphs:
    # Single graph determined by both selections
    fig = px.line(
        df_state,
        x="Year",
        y=demographic,
        title=f"{demographic} of {state}"
    )
    fig.update_yaxes(rangemode="tozero")
    st.plotly_chart(fig, use_container_width=True)

with tab_table:
    st.write("All Data")
    st.dataframe(df, use_container_width=True)