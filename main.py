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
latex_expr = "a^2 + b^2 = c^2"
st.write(f"The pythagorean theorem is given by the equation ${latex_expr}$.")
