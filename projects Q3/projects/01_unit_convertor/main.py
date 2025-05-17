import streamlit as st


def unit_converter(value, unit_from , unit_to):

    conversion = {
        "meters_kilometers" : 0.001,
        "kilometers_meters" : 1,
        "grams_kilograms" : 0.001,
        "kilograms_grams" : 1000,

    }

    key = f"{unit_from}_{unit_to}"

    if key in conversion:
        conversion = conversion[key]
        return value * conversion
    else:
        return "Conversion not supported"
    

st.title("Unit Converter")
value = st.number_input("Enter the value to convert",min_value=1.0 , step=1.0)
unit_from = st.selectbox("From", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("To", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    result = unit_converter(value, unit_from, unit_to)
    st.write(f"Converted value : {result}")