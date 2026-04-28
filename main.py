import streamlit as st
st.title("streamsambitlit")
st.write("hallo, use streamlit")

name= st.text_input(" enyter name")
age = st.number_input("your age")

if st.button("submit"):
  st.write(f"hallo,{name}! welcome to streamlit")
  if age >= 18:
    st.write("u can vote")
  elif age >= 65:
    st.write("u dead")
  else:
    st.write("u cannot vote")
