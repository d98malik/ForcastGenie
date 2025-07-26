from fbprophet import Prophet
import pandas as pd
import plotly.graph_objs as go

def forecast_stock(df):
    df = df.rename(columns={'Date': 'ds', 'Close': 'y'})
    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['ds'], y=df['y'], name='Actual'))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], name='Forecast'))
    return fig
