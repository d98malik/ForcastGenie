import streamlit as st
from app.forecast import forecast_stock
from app.genai_query import query_to_code
from app.retriever import retrieve_context
from app.utils import get_stock_data

st.title("📊 ForecastGenie – GenAI Time Series Assistant")

query = st.text_input("Ask your financial question:")
ticker = st.text_input("Enter stock ticker (e.g., AAPL):", "AAPL")

if query and ticker:
    context = retrieve_context(query)
    st.markdown("**Context Retrieved:**")
    st.write(context)

    df = get_stock_data(ticker)
    fig = forecast_stock(df)
    st.plotly_chart(fig)

    response = query_to_code(query)
    st.markdown("**GenAI Response:**")
    st.code(response)
