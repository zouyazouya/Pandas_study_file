'''
streamlit run C:\Project2021\Python\example_plotly.py
'''
import os
# import plotly.graph_objects as go
# import plotly.express as px
import pandas as pd
import numpy as np
import streamlit as st



class target_pandas(object):    
    def use_pandas(self):
        st.header("常用函数")
        tab1,tab2,tab3,tab4 = st.tabs(["常用统计函数","数据类型转换","读取保存数据","其他常用函数"])
        #测试用数据
        data = {'Name':['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
        'Lee','David','Gasper','Betina','Andres'],
        'Age':[25,26,25,23,30,29,23,34,40,30,51,46],
        'Rating':[4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65]}
        df2=pd.DataFrame(data)
         
        with tab1:
            st.subheader("基本统计函数")
            fun_data = {
                        "编号":[1,2,3,4,5,6,7,8,9,10,11,12],
                        "属性或方法":["sum()方法","mean()方法","count()方法","median()方法","mode()方法","std()方法",
                                    "min()方法","max()方法","abs()方法","prod()方法","cumsum()方法","cumprod()方法"],
                        "描述":["返回所请求轴的值的总和。 默认情况下，轴为索引(axis=0)。",
                                "返回平均值",
                                "返回非空观测数量",
                                "返回所有值的中位数",
                                "返回所有值的中位数",
                                "返回值的标准偏差",
                                "返回所有值中的最小值",
                                "返回所有值中的最大值",
                                "返回绝对值",
                                "返回数组元素的乘积",
                                "返回累计总和",
                                "返回累计乘积"]
                        }
            df=pd.DataFrame(fun_data).set_index("编号")
            st.table(df)
            
            fun_num = st.selectbox("选择属性或方法的编号",range(1,13))
            st.write(df2.head(1))
            if fun_num==1:
                st.code('''
        #统计全部或部分列的总和
            df.sum()
            df[["Age","Rating"]].sum()
        #执行行的合计时，增加axis=1的参数
            df.sum(axis=1)        
                ''')
                st.text(df2.sum())
                st.write(df2[["Age","Rating"]].sum())
                st.write(df2.sum(axis=1))
            elif fun_num==2:
                st.code('''
        #统计全部列的平均值
            df.mean()
        #执行行的平均值时，增加axis=1的参数
                ''')
                st.write(df2.mean())
                
        with tab2:
            st.subheader("数据类型转换")
                
        with tab3:
            st.subheader("读取保存数据")
            fun_data = {
                        "编号":[1,2,3,4,5,6,7,8,9,10,11,12],
                        "属性或方法":["read_csv()方法","","","","","",
                                    "to_csv()方法","","","","",""],
                        "描述":["",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                ""]
                        }
            df=pd.DataFrame(fun_data).set_index("编号")
            st.table(df)
            
            fun_num = st.selectbox("选择属性或方法的编号",range(1,13),key=3)
            st.write(df2.head(1))
            
        with tab4:
            st.subheader("其他常用函数")
            fun_data = {
                        "编号":[1,2,3,4,5,6,7,8,9,10,11,12],
                        "属性或方法":["describe()方法","head()方法","tail()方法","value_counts()方法","","",
                                    "","","","","",""],
                        "描述":["计算有关DataFrame列的统计信息的摘要",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                ""]
                        }
            df=pd.DataFrame(fun_data).set_index("编号")
            st.table(df)
            
            fun_num = st.selectbox("选择属性或方法的编号",range(1,13),key=2)
            st.write(df2.head(1))
            if fun_num==1:
                st.code('''
    #计算有关DataFrame列的统计信息的摘要。
        df.describe()
    #include是用于传递关于什么列需要考虑用于总结的必要信息的参数。获取值列表; 默认情况下是”数字值”。
    #   object - 汇总字符串列
    #   number - 汇总数字列
    #   all - 将所有列汇总在一起(不应将其作为列表值传递)
        df.describe(include=['object'])
        df.describe(include='all')
                ''')        
                st.table(df2.describe())
                st.text(df2.describe(include='all'))
            
    def use_index(self):
        st.header("索引相关语法")
        st.subheader("1、设置DF的索引列")
        data={
            "姓名":["小张","小王","小李","小赵"],
            "性别":["男","女","男","女"],
            "年龄":[18,19,20,18]
        }
        df=pd.DataFrame(data)
               
        tab1,tab2,tab3 = st.tabs(["原DF","设置索引列为数据列","将索引列恢复为数据列"])
        with tab1:
            html_df=df.to_html()
            st.markdown(html_df,unsafe_allow_html=True)
        with tab2:
            st.text('''将原DF的"姓名"字段设置为索引''')
            st.code('''df.set_index("姓名",inplace=True)''')
            df2 = df.set_index("姓名")
            html_df2 = df2.to_html()
            st.markdown(html_df2, unsafe_allow_html=True)
        with tab3:
            st.code('''df2.reset_index(inplace=True)''')
            df3 = df2.reset_index()
            st.dataframe(df3.head())

    def use_datetime(self):
        st.header("时间日期相关语法")
        st.subheader("1、生成时间日期列表")
        st.code('''
#生成指定时间的列表
    date_range = pd.date_range(start='2021-10-01',end='2021-10-31')
#相当于下列代码
    date_range = pd.date_range(start='2021-10-01', periods=31)
#返回该日期是1年中的第几天
    df['day_of_year']= df['day'].dt.dayofyear
        ''')
        if st.checkbox("显示结果",key=1):
            date_range = pd.date_range(start='2021-10-01', end='2021-10-31')
            df = pd.DataFrame(date_range, columns=["day"])
            df['day_of_year']= df['day'].dt.dayofyear
            st.table(df.head())
            st.text(df.dtypes)

        st.code('''
#生成一年中每周一的日期
    date_range = pd.date_range(start='2021-01-01',end='2021-12-31',freq="W-MON")
    date_range = pd.date_range(start='2021-01-01', periods=52, freq="W-MON")
        ''')
        if st.checkbox("显示结果",key=2):
            date_range = pd.date_range(start='2021-01-01', end='2021-12-31', freq="W-MON")
            df = pd.DataFrame(date_range,columns=["DateTime"])
            st.table(df.head())

        st.code('''
#生产每小时间隔的时间列表
    date_range = pd.date_range(start="2021-10-01",periods=24,freq='H')
    date_range = pd.date_range(start="2021-10-01",end="2021-10-03",freq='H', closed='left')
    #加closed='left'表示不包含end的日期
        ''')
        if st.checkbox("显示结果", key=3):
            date_range = pd.date_range(start="2021-10-01", periods=24, freq='H')
            df=pd.DataFrame(date_range)
            st.table(df.head())
            
        st.code('''
#新增数据年份，小时列
    df["Year"]=df["Date"].dt.year
    df["Hour"]=df["Date"].dt.hour
        ''')
        if st.checkbox("显示结果", key=4):
            date_range = pd.date_range(start="2021-10-01", periods=24, freq='H')
            df=pd.DataFrame(date_range,columns=["Date"])
            df["Year"]=df["Date"].dt.year
            df["Month"]=df["Date"].dt.month
            df["Hour"]=df["Date"].dt.hour
            st.table(df.head())
            
    def use_groupby(self):
        pass

def main():
    st.title("我的笔记")
    st.markdown("---")

    st.sidebar.header("相关语法")
    tp = target_pandas()
    if st.sidebar.checkbox("Pandas相关"):
        selected_item = st.sidebar.radio("",[
            "常用函数",
            "索引列",
            "时间日期",
            "分类汇总"
            ])
        if selected_item=="常用函数":
            tp.use_pandas()
        elif selected_item=="索引列":
            tp.use_index()
        elif selected_item=="时间日期":
            tp.use_datetime()
        elif selected_item=="分类汇总":
            tp.use_groupby()
    elif st.sidebar.checkbox("numpy相关"):
        pass
    elif st.sidebar.checkbox("Streamlit相关"):
        pass
    elif st.sidebar.checkbox("Plotly相关"):
        pass

if __name__ == '__main__':
    main()
