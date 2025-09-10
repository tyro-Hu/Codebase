import streamlit as st
import pandas as pd

# 1. 向界面上输出字符串
st.write("## 早上好")

# 或者不写st.write，直接写字符串，会自动调用st.write
"## 早上好"

# 2. 显示变量值
a = 1 + 1
a

[1, 2, 3]


{
"1" : "a", 
"2" : "b"
 }

# 3. 展示网页大标题
st.title("我的个人网站💡")

# 4. 展示图片
st.image("头像.png", width=200)

# 5. 展示表格数据
df = pd.DataFrame({
    "学号" : [1, 2, 3],
    "姓名" : ["张三", "李四", "王五"],
    "性别" : ["男", "女", "男"]
})

st.dataframe(df) # 可交互表格
st.table(df) # 静态表格

# 6. 展示分隔线
st.divider()


# 运行：在终端运行streamlit run 文件名.py