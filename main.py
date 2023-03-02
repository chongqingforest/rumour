import streamlit as st
import pandas as pd
import sqlite3

# 创建流言列表
rumour_list = []


# 创建流言类
class Rumour :
    def __init__(self, name, date, position) :
        self.name = name
        self.date = date
        self.position = position


# 添加流言的函数
def add_rumour(name, date, position) :
    con = sqlite3.connect('rumour.db')
    cur = con.cursor()
    rumour = Rumour(name, date, position)
    # print(rumour.name,rumour.date,rumour.position)
    sql = f'''insert into rumour (name, date,position) values ("{rumour.name}","{rumour.date}","{rumour.position}")'''
    
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()
    
    # rumour_list.append(rumour)
    # print(rumour_list,len(rumour_list))


# 显示流言列表函数
def show_rumour_list() :
    con = sqlite3.connect('rumour.db')
    cur = con.cursor()
    sql = f'''select * from rumour'''
    
    cur.execute(sql)
    result = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    print(result)
    
    df = pd.DataFrame(result, columns=['序号', '话题', '日期', '内容'])
    # st.dataframe(df)
    if len(df) == 0 :
        st.write('列表为空！')
        # df = pd.DataFrame(result, columns=['序号','话题', '日期', '内容'])
        # st.dataframe(df)
    else :
        # df = pd.DataFrame(result, columns=['序号','话题', '日期', '内容'])
        st.dataframe(df)


# 添加流言界面
def add_rumour_page() :
    st.write('添加新流言')
    name = st.text_input('话题')
    date = st.date_input('日期')
    position = st.text_input('内容')
    if st.button('添加') :
        add_rumour(name, date, position)
        st.success('添加成功！')


# 显示流言列表界面
def show_rumour_list_page() :
    st.write('流言列表')
    show_rumour_list()
    # print(test)


# 主程序
def main() :
    st.title('匿名流言')
    menu = ['添加流言', '流言列表']
    choice = st.sidebar.selectbox('选择菜单', menu)
    if choice == '添加流言' :
        add_rumour_page()
    elif choice == '流言列表' :
        show_rumour_list_page()


if __name__ == '__main__' :
    # sqlite3.connect('rumour.db')
    main()
