import streamlit as st
st.title("streamsambitlit")
st.write("hallo, use streamlit")

name= st.text_input(" enyter name")
age = st.number_input("your age")

if st.button("submit"):
  st.write(f"hallo,{name}! welcome to streamlit")
  if age >= 18 and age <65:
    st.write("u can vote")
  elif age >= 65:
    st.write("u dead")
  elif age < 0:
    st.write(" u are not born")
  else:
    st.write("u cannot vote")
st.caption("smol  text")
st.write(st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    '''))
