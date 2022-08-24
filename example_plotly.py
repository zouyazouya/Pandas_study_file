'''
streamlit run d:\lyj\dataanalysis\example_plotly.py
在启动本地任务时，需要将CMD地址改为CD D:\LYJ\DataAnalysis
https://plotly.com/python/plotly-express/
'''
import os
# import plotly.graph_objects as go
# import plotly.express as px
import pandas as pd
import numpy as np
import streamlit as st

def create_df1():
    data={
        "姓名":["小张","小王","小李","小赵"],
        "性别":["男","女","男","女"],
        "年龄":[18,19,20,18]
    }
    df=pd.DataFrame(data)
    return df

def use_index():
    st.header("索引相关语法")
    st.subheader("1、设置DF的索引列")

    df=create_df1()
    html_df=df.to_html()
    st.markdown(html_df,unsafe_allow_html=True)
    st.text("原DF")

    df.set_index("姓名",inplace=True)
    html_df2 = df.to_html()
    st.markdown(html_df2, unsafe_allow_html=True)
    st.text('''将原DF的"姓名"字段设置为索引''')

def use_datetime():
    st.header("时间日期相关语法")
    st.subheader("1、生成时间日期列表")
    st.code('''
    #生成指定时间的列表
    date_range = pd.date_range(start='2021-10-01',end='2021-10-31')
    #相当于下列代码
    date_range = pd.date_range(start='2021-10-01', periods=31)
    ''')
    if st.checkbox("显示结果",key=1):
        date_range = pd.date_range(start='2021-10-01', end='2021-10-31')
        df = pd.DataFrame(date_range, columns=["DateTime"])
        df
        st.text(df.dtypes)

    st.code('''
    #生成一年中每周一的日期
    date_range = pd.date_range(start='2021-01-01',end='2021-12-31',freq="W-MON")
    date_range = pd.date_range(start='2021-01-01', periods=52, freq="W-MON")
    ''')
    if st.checkbox("显示结果",key=2):
        date_range = pd.date_range(start='2021-01-01', end='2021-12-31', freq="W-MON")
        df = pd.DataFrame(date_range,columns=["DateTime"])
        df

    st.code('''
    date_range = pd.date_range(start="2021-10-01",periods=24,freq='H')
    date_range = pd.date_range(start="2021-10-01",end="2021-10-03",freq='H', closed='left')
    ''')
    if st.checkbox("显示结果", key=3):
        date_range = pd.date_range(start="2021-10-01", periods=24, freq='H')
        df=pd.DataFrame(date_range)
        df

def main():
    st.title("Pandas")

    st.sidebar.header("相关语法")
    selected_item = st.sidebar.radio("",[
        "索引",
        "时间日期",
        "3"
        ])
    if selected_item=="索引":
        use_index()
    elif selected_item=="时间日期":
        use_datetime()



if __name__ == '__main__':
    main()
