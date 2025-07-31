import streamlit as st

st.title("Basic Power Calculator")
st.write("Enter a number to calculate it's square, cube and fifth power")

n = st.number_input("Enter a number", value = 1, step = 1)

square = n ** 2
cube = n ** 3
fifth_power = n ** 5

st.write(f"The Square of {n} is : {square}")
st.write(f"The Cube of {n}: {cube}")
st.write(f"The Fifth Power of {n}: {fifth_power}")