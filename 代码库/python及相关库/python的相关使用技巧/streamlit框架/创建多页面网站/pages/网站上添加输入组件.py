import streamlit as st

# 1. 展示输入文本框
name = st.text_input("请输入你的名字：")
if name:
    st.write(f"你好，{name}")


# 注意：一下情况下程序重新执行
# 1）. 代码重新保存执行
# 2）. 用户与网站上的交互组件发生交互

st.divider()

# 2. 展示输入密码框
password = st.text_input("请输入密码：", type="password")

st.divider()

# 3. 展示输入多行文本框
text = st.text_area("请输入你的简介：")

st.divider()

# 4. 展示输入数字框
age = st.number_input("请输入你的年龄：", min_value=0, max_value=120, value=18, step=1)
st.write(f"你的年龄是：{age}")

st.divider()

# 5. 展示勾选框
agree = st.checkbox("同意协议")
if agree:
    st.write("你已同意协议")

st.divider()

# 6. 展示按钮
submited = st.button("提交")
if submited:
    st.write("提交成功")

st.divider()

# 7. 展示单选框
options = ["男", "女", "跨性别"]
selected_option = st.radio("请选择一个选项：", options, index=0)
st.write(f"你选择的性别是：{selected_option}")

st.divider()

# 8. 展示单选下拉框
options = ["男", "女", "跨性别"]
selected_option = st.selectbox("请选择一个性别：", options)
st.write(f"你选择的性别是：{selected_option}")

st.divider()

# 9. 展示多选下拉框
selected_options = st.multiselect("请选择多个选项：", options)
st.write(f"你选择的选项是：{selected_options}")

st.divider()

# 10. 展示滑块
value = st.slider("请选择一个值：", min_value=0, max_value=100, value=50)
st.write(f"你选择的值是：{value}")

st.divider()

# 11. 展示文件上传框
uploaded_file = st.file_uploader("请上传一个文件：", type=["png", "jpg", "jpeg"]) # 返回的是uploadFile类型的对象实例
if uploaded_file:
    st.write(f"你上传的文件是：{uploaded_file.name}")
    st.write(f"你上传的文件类型是：{uploaded_file.type}")