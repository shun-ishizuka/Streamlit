import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st
import plotly.express as px

st.title('米国株価可視化アプリ')

st.sidebar.write("""
# 米国株価
こちらは株価可視化ツールです。以下のオプションから表示日数を指定してください。

""")

st.sidebar.write("""
## 表示日数選択
""")

# daysとして表示日数を格納
days = st.sidebar.slider('日数',1,50,20)

st.write(f"""
### 過去 **{days}日間** の米国株価
""")

# ↓読み取り速度の向上
@st.cache
def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df, hist])
    return df
try:
    st.sidebar.write("""
    ## 株価の範囲指定
    """)

    y_min , y_max = st.sidebar.slider(
        '範囲を指定してください',
        0.0,3500.0,(0.0,3500.0)
    )


    tickers = {
        'apple': 'AAPL',
        'facebook': 'FB',
        'google': 'GOOGL',
        'microsoft': 'MSFT',
        'netflix': 'NFLX',
        'amazon': 'AMZN',
        'Tesla':'TSLA',
        'AT&T':'T',
        'Alibaba':'BABA',
        'Starbucks':'SBUX'
    }


    df = get_data(days, tickers)

    companies = st.multiselect(
        '会社名を選択してください',
        list(df.index),
        ['google','apple','facebook','amazon']
    )

    if not companies:
        st.error('少なくとも一社は選んでください。')
    else:
        data = df.loc[companies]
        st.write("""
        ### 株価(USD)
        ※終値
        """
        ,data.sort_index())
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['Date']).rename(
        columns={'value': 'Stock Prices(USD)'}
        )

        chart = (
            # alt.Chart(上記で得たデータを入れる)
            alt.Chart(data)
            # mark_line → 折れ線グラフ , opacity 透明度 , clip=True で表外のグラフは表示しない。
            .mark_line(opacity=0.8, clip=True)
            #軸の設定
            .encode(
                # :T は設定。タイムの意味？
                x="Date:T",
                # alt.Y()でほかの設定もまとめて行うことができる。 :Q は定量的 , scale=alt.Scale(domain=[ , ])で最大値、最小値を設定
                y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[y_min, y_max])),
                # グラフで分ける
                color='Name:N'
            )
        )
        st.altair_chart(chart,use_container_width=True)

except:
    st.error("エラーが起きているようです。リロードしてみてください。")



st.write('-------------\n')
st.write("""
## その他米国株価の可視化(50日間分)
""")
Ticker_code = st.text_input("ティッカーシンボルを入力してください。")

st.write("""
ティッカーシンボル一覧  
https://eoddata.com/symbols.aspx?AspxAutoDetectCookieSupport=1
""")

hist = yf.Ticker(Ticker_code).history(period='50d')
hist_new = hist.reset_index()

if Ticker_code:
    x = hist_new['Date']
    y = hist_new['Close']

    st.write(f""" ## {Ticker_code}の株価""")
    st.write('・ カーソルで範囲を指定することでズームすることができます。')
    st.write(' ・カーソルをグラフに合わせると日付と株価を見ることができます')   
    st.write('※元の図に戻したいときは図上でダブルクリックすると戻ります。')

    st.write(
         px.line(x=x,y=y)
    )