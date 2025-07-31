import streamlit as st

# This is a basic streamlit app which calculates the square, cube, and fifth power of a number entered by the user.
st.title("Basic Power Calculator")
st.write("Enter a number to calculate it's square, cube and fifth power")

# Taking input from the user
n = st.number_input("Enter a number", value = 1, step = 1)

# Calculating square, cube, and fifth power
square = n ** 2
cube = n ** 3
fifth_power = n ** 5

# Displaying the results
st.write(f"The Square of {n} is : {square}")
st.write(f"The Cube of {n}: {cube}")
st.write(f"The Fifth Power of {n}: {fifth_power}")