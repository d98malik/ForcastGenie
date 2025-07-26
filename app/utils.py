import yfinance as yf

def get_stock_data(ticker):
    df = yf.download(ticker, period="6mo")
    df.reset_index(inplace=True)
    return df[['Date', 'Close']]
