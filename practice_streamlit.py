import streamlit as st
import numpy as np 
import pandas as pd
from PIL import Image
import time

# WEBに表示するときは以下のコマンドを左上のTermnalに打ち込む
## streamlit run main.py 

st.title('Streamlit 試作')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # 数字が増えていく
    latest_iteration.text(f'Iteration {i + 1}')
    # 進捗が増えていっている
    bar.progress(i+1)
    # 速さ調整
    time.sleep(0.05)

'Done!!!'

left_column,center_column ,right_column = st.columns(3)
left_button = left_column.button('右カラムに文字を表示')

if left_button:
    right_column.write('ここは右カラムです')
    center_column.write('ここは中央カラムです')

expander = st.expander('問い合わせ内容')
update  = expander.button('契約更新')
cancel  = expander.button('契約解約')
confirm = expander.button('契約内容確認')
others  = expander.button('その他')

if update:
    st.write('契約の更新はHPから可能です。')
elif cancel:
    st.write('今ならお得なプランがご利用可能です。')
    st.write('解約する方はお電話にて承っております。')
elif confirm:
    st.write('現在の契約内容はHPから閲覧可能です。')
elif others:
    st.write('カスタマーサポートにお電話ください。')



# condition = st.slider('あなたの調子は？',0,10,step=2)
# text = st.text_input('あなたの趣味を教えてください。')
# 'コンディション',condition,
# 'あなたの趣味は',text,'です。'


# if st.checkbox('show image'):
#     img = Image.open('red_brige.jpg')
#     st.image(img,caption='matusima',use_column_width=True)


# option  = st.selectbox(
#     'あなたが好きな数字を教えてください、',

#     # option はリストで指定する。
#     list(range(1,11)))
 
 # print文など使わなくても表示可能
# 'あなたの好きな数字は',option,'です。'

## マップに点を打てる
# df = pd.DataFrame (
#     np.random.rand(100,2)/[50,50]+[35.60,139.70],
#     columns=['lat','lon']
# )
# st.map(df)


# 動的なテーブル
# st.dataframe(df.style.highlight_max(axis=0))
# 静的なテーブル
# st.table(df.style.highlight_max(axis=0))



## コメントアウトで文字を打ち込める
## ```←でコードの表示をすることができる。

# """

# # 大
# ## 中
# ### 小

# ```python
# import streamlit as st
# import numpy as np 
# import pandas as pd

# df = pd.DataFrame ({
#     '1列目' : [1,1,3,3],
#     '2列目' : [3,4,5,6]
# })
# """

