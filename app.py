import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import streamlit as st

pio.templates.default = "seaborn"

df = pd.read_csv("Data_3-15-2023---346.csv")
df = df.drop(df.iloc[22].name)

def bar_chart(data: pd.DataFrame, column_name: str) -> go.Figure:
    default_color = "blue"
    colors = {"Metropolitan State University of Denver": "red"}

    color_discrete_map = {
        c: colors.get(c, default_color) for c in data["Institution Name"]
    }

    fig = px.bar(
        data,
        x="Institution Name",
        y=column_name,
        color="Institution Name",
        color_discrete_map=color_discrete_map,
        height=1000,
    )
    fig.update_traces(showlegend=False)
    fig.update_layout(xaxis={"categoryorder": "total ascending"})

    return fig

metrics = ['Average net price-students awarded grant or scholarship aid  2020-21 (SFA2021)',
       'Percent of full-time first-time undergraduates awarded any financial aid (SFA2021)',
       'Average amount of federal  state  local or institutional grant aid awarded (SFA2021)',
       'Graduation rate  total cohort (DRVGR2021)',
       'Total FTE staff (DRVHR2021)',
       'Average salary equated to 9 months of full-time instructional staff - all ranks (DRVHR2021)',
       'Average salary equated to 9 months of full-time instructional staff - professors (DRVHR2021)',
       'Average salary equated to 9 months of full-time instructional staff - associate professors (DRVHR2021)',
       'Average salary equated to 9 months of full-time instructional staff - assistant professors (DRVHR2021)',
       'Average salary equated to 9 months of full-time instructional staff - instructors (DRVHR2021)',
       'Average salary equated to 9 months of full-time instructional staff - lecturers (DRVHR2021)']  

st.title("Quick IPEDS data comparisons")

metric = st.selectbox("Comparison Metric", metrics)

if metric:
  st.plotly_chart(bar_chart(df, metric))
