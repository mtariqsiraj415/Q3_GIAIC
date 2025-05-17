# ------------------------- Growth mindset challenge ------------------------- #


#imports
import streamlit as st
import pandas as pd
import os
from io import BytesIO




# Set up our App
st.set_page_config(page_title="Growth mindset challenge" ,layout="wide")
st.title("Growth Mindset Challenge")
st.write("This app is a challenge to help you develop a growth mindset")



# File uploader
uploaded_files = st.file_uploader("Upload your files (CSV or Excel) :" , type=["csv" , "xlsx"] , accept_multiple_files=True)



if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type :{file_ext}")
            continue
        

        # Display info about the file
        st.write(f"File name : {file.name}")
        st.write(f"File Size : {file.size/1024}")


        # Show 5 rows of our df
        st.write("Preview of the uploaded file:")
        st.dataframe(df.head())


        #options for deta cleaning
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1 ,col2 = st.columns(2)

            with col1:
                if st.button(f"Rmove Dulicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Demoved!")

            with col2:
                if st.button(f"File Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols]).mean()
                    st.write("Missing Value have been Filed!")

            # st.write("Preview of the uploaded file:")
            # st.dataframe(df.head())

        
        #Chosse Specific Colums to Keep or Convert
        st.subheader("Select Colums to Convert")
        colums = st.multiselect(f"Choose Colums for {file.name}",df.columns , default=df.columns)
        df = df[colums]


        # Create Some Visualization
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include="number").iloc[::2])



        # Convert the File  ==> CSV to Excel
        st.subheader("Converstion Options")
        convestion_type = st.radio(f"Convert {file.name} to:" , ["CSV","Excel"],key=file.name)
        if st.button(f"Conert file:{file.name}"):
            buffer = BytesIO()

            if convestion_type == "CSV":
                df.to_csv( buffer , index=False)
                file_name = file.name.replace(file_ext , ".cvs")
                mime_type = "text/csv"

            elif convestion_type == "Excel":
                df.to_excel(buffer , index=False)
                file_name = file.name.replace(file_ext , "xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)


            # Download Butten
            st.download_button("Click to download", buffer, file_name=file_name, mime=mime_type)
            
st.success("All files processed successfully! 🎉🎉")