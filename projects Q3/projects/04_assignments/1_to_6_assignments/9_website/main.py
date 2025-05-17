import streamlit as st
import streamlit_option_menu as menu_option

# Add some CSS for styling

st.markdown("""

""")

st.markdown("""
    <style>
        # * {
        #     font-family: 'Arial', sans-serif;
        #     background-color: black ;
        #     color: white;
        # }
        .main-header {
            color: #333;
            text-align: center;
            font-size: 2em;
            margin-bottom: 20px;
        }
        .page {
            padding: 20px;
        }
        .footer {
            background-color: #333;
            color: red;
            padding: 10px;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.write("Thems change")
thems =  st.sidebar.radio("Select",["White" , "Black"])

if thems == "Black":
    st.markdown("""

<style>

        * {
            font-family: 'Arial', sans-serif;
            background-color: black ;
            color: white;
        }

</style>



""" , unsafe_allow_html=True)


# Define pages
def home():
    st.markdown('<h1> Hello My Name is <span style="color: aqua;"> Muhammad Shahzad </span> </h1>', unsafe_allow_html=True)
    
    st.image("me.jpeg", width=200)
    st.markdown("""
        <div class="links">
            <a href="https://github.com/shahzad006" target="_blank">Github</a><br>
            <a href="https://www.linkedin.com/in/muhammad-shahzad-9b86892b9/" target="_blank">Linkedin</a><br>
            
        </div>
        <style>
            .links a {
                color: #1f77b4;
                text-decoration: none;
                font-size: 1.2em;
            }
            .links a:hover {
                text-decoration: underline;
                color : red;
            }
        </style>
                
    """, unsafe_allow_html=True)

    
    st.markdown("""
        <h1 class="project">Projects</h1>
        <h3>Project 1: Mad libs Python Project</h3>
        <a href="https://colab.research.google.com/drive/1LorSXm4zkKeZ_TyUyNshqtcbC9vD0lKs?usp=sharing" target="_blank">Google colab</a>  <br>
        <a href="https://github.com/shahzad006/python_project/tree/main/1_madlibs" target="_blank">Github link </a>

                
        <h3>Project 2: Guess the Number Game Python Project (computer)</h3>
        <a href="https://colab.research.google.com/drive/1af97ycRQyzL38PtF_GY-QHws02sX1Cxg?usp=sharing" target="_blank">Google colab</a>  <br>
         <a href="https://github.com/shahzad006/python_project/tree/main/2_guess_the_number(computer)" target="_blank">Github link </a>


        <h3>Project 3: Guess the Number Game Python Project (user)</h3>
        <a href="https://colab.research.google.com/drive/1jxEqPd2Yp5N6fU6jRXYNyx_HW9eIl-67?usp=sharing" target="_blank">Google colab</a>  <br>
        <a href="https://github.com/shahzad006/python_project/tree/main/3_guess_the_number(user)" target="_blank">Github link </a>

    

        <h3>Project 4: Rock, paper, scissors Python Project</h3>
        <a href="https://colab.research.google.com/drive/1pMaU13OQ5-JjyKW9K1NEiLp3wqqmSdvH?usp=sharing" target="_blank">Google colab</a>  <br>
        <a href="https://github.com/shahzad006/python_project/tree/main/4_rock_paper_scissors" target="_blank">Github link </a>


        <h3>Project 5: Hangman Python Project</h3>
        <a href="https://colab.research.google.com/drive/1ivkGoBfJPTMY0Hk7A_XNmombAuvDzz5U?usp=sharing" target="_blank">Google colab</a>  <br>
        <a href="https://github.com/shahzad006/python_project/tree/main/5_hangman" target="_blank">Github link </a>

        <h3>Project 6: Countdown Timer Python Project</h3>
        <a href="https://colab.research.google.com/drive/1OHFItzQ9EYBsRy16Hfyy7_ys8_j6L4w8?usp=sharing" target="_blank">Google colab</a>  <br>
        <a href="https://github.com/shahzad006/python_project/tree/main/6_countdown_timer" target="_blank">Github link </a>

        <h3>Project 7: Password Generator Python Project</h3>
        <a href="https://colab.research.google.com/drive/1hecIcSTnZtat33IBohm8IsRC74KkeTOx?usp=sharing" target="_blank">Google colab</a>  <br>
        <a href="https://github.com/shahzad006/python_project/tree/main/7_password_generator" target="_blank">Github link </a>
                

        <h3>Project 8: Create a Python Streamlit BMI Calculator Web App</h3>
        <a href="https://github.com/shahzad006/python_project/tree/main/8_streamlit_bmi_calculator" target="_blank">Github link </a>
                

                
        <h3>Project 9: Build a Python Website</h3>
       <p>This Website😊</p>
                

        


                 
                

        

    
        
                

            
                
            
        <style>
                
                .project{
                display: flex;
                align-items: center;
                justify-content: center;
                

                }

            .links a {
                color: #1f77b4;
                text-decoration: none;
                font-size: 1.2em;
            }
            .links a:hover {
                text-decoration: underline;
                color : red;
            }
        </style>
    """, unsafe_allow_html=True)










    

def about():
    st.title('About Us')
    st.markdown("""
                
                <h2>Introducion</h2>
                <p>👦 I am a Website Developer , Where  I am currently working on a AI 🤖 from <a href="https://www.piaic.org/" target="_blank">PIAIC</a></p>
                <h2>Our mission</h2>
                <p>Our mission is to help people learn new skills and grow their careers. We believe that everyone should have access to quality education and resources.</p>
                <h2>Our vision</h2>
                <p>Our vision is to create a world where everyone has the opportunity to reach their full potential. We want to empower people to achieve their goals and dreams.</p>
        

    """, unsafe_allow_html=True)
    

def contact():
    st.title('Contact Us')
    st.text_input("Enter your name ",placeholder="HERE TYPE.....")
    st.text_input("Enter your email ",placeholder="HERE TYPE....." , max_chars=15)
    st.text_area("Enter your msg ",placeholder="HERE TYPE....." , max_chars=200)
    st.button("SEND")





page = menu_option.option_menu(
        menu_title = None,
        options=["Home","About" ,"Contact"],
        icons=["house","phone","contact"],
        orientation="horizontal"
    )

# Render the selected page
if page == "Home":
    home()
elif page == "About":
    about()
elif page == "Contact":
    contact()

# Add footer
# st.markdown('<div class="footer">Footer content goes here</div>', unsafe_allow_html=True)
