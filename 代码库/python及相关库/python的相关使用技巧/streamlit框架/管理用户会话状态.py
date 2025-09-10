import streamlit as st

# 为什么需要管理会话状态举例
# a = 0
# clicked = st.button("加1")
# if clicked:
#     a += 1
# st.write(a)

# 上面的例子中，无论怎么点击，值永远为1. 因为streamlit每次刷新页面，都会重新运行代码，所以变量a会重新初始化为0
# 所以需要管理用户的会话状态，只要用户不把页面关掉，就保存用户交互过程中的变量

# 打印会话状态
print(st.session_state)

if "a" not in st.session_state:
    st.session_state.a = 0
clicked = st.button("加1")
if clicked:
    st.session_state.a += 1
st.write(st.session_state.a)


