import streamlit as st
import time


st.set_page_config(page_title="BMI Calculator" , layout="centered")

st.title("BMI Calculator")
st.markdown("This is a simple BMI Calculator. Please enter your height and weight to calculate your BMI.")


col1, col2 = st.columns(2)

with col1:
    height = st.number_input("Enter your Height (kg) :" , min_value=1.0 , max_value=250.0 , format="%.2f") 
with col2:
    weight = st.number_input("Enter your Weight (m) :" , min_value=1.0 ,max_value=200.0, format="%.2f") 



if st.button("Calculate BMI"):
    bmi = weight / ((height/100) **2)
    st.write("Calculating your BMI...")
    time.sleep(2)
    st.write(f"Your BMI is : {bmi:.2f}")



    if bmi < 18.5:
        st.error("You are Underweight")
    elif 18.5 <= bmi < 25:
        st.success("You have Normal weight")
    elif 25 <= bmi < 30:
        st.warning("You are Overweight")
    else:
        st.error("You are Obese")


    st.write("******************  BMI Categories ******************")
    st.write("- Underweight : BMI less then 18.5")
    st.write("- Normal weight : BMI between 18.5 and 24.9")
    st.write("- Overweight : BMI between 25 and 29.9")
    st.write("- Obesity : BMI 30 or greater")

