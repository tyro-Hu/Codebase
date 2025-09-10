import streamlit as st

# 1. 展示侧边栏
with st.sidebar:
    # 展示输入文本框
    name = st.text_input("请输入你的名字：")
    if name:
        st.write(f"你好，{name}")


st.divider()

# 2. 将页面分成三列
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("第一列")
    # 展示输入密码框
    password = st.text_input("请输入密码：", type="password")

with col2:
    st.write("第二列")
    # 展示输入多行文本框
    text = st.text_area("请输入你的简介：")

with col3:
    st.write("第三列")
    # 展示输入日期框
    date = st.date_input("请输入你的生日：")
    st.write(f"你的生日是：{date}")


# 3. 点击不同的选项卡，显示不同的内容
tab1, tab2, tab3 = st.tabs(["年龄", "性别", "提交"])

with tab1:
    # 展示输入数字框
    age = st.number_input("请输入你的年龄：", min_value=0, max_value=120, value=18, step=1)
    st.write(f"你的年龄是：{age}")

with tab2:
    options = ["男", "女", "跨性别"]
    selected_option = st.selectbox("请选择一个性别：", options)
    st.write(f"你选择的性别是：{selected_option}")

with tab3:
    # 展示按钮
    submited = st.button("提交")
    if submited:
        st.write("提交成功")

st.divider()

# 4. 折叠展开组件
with st.expander("上传文件"):
    # 展示文件上传框
    uploaded_file = st.file_uploader("请上传一个文件：", type=["png", "jpg", "jpeg"]) # 返回的是uploadFile类型的对象实例
    if uploaded_file:
        st.write(f"你上传的文件是：{uploaded_file.name}")
        st.write(f"你上传的文件类型是：{uploaded_file.type}")


