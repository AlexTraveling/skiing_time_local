import streamlit as sl
import subprocess

from help_page import step_1, step_2, step_3


# Topbar Section
def top_section():

   sl.markdown('''     
   <style>

   .title {
      text-align: center;
   }
   .describe {
      text-align: center;
      color: grey;
   }

   </style>

   ''', unsafe_allow_html=True)

   column = sl.columns([2, 2, 1, 1, 1])

   with column[0]:
      logo_path = 'home_page_material/skiing_time_logo_2.png'
      sl.image(logo_path)

   with column[2]:
      help_page_url = 'https://skiing-time-assist.streamlit.app/'
      sl.markdown(f'[Help]({help_page_url})')
   
   with column[3]:
      about_us_page_url = 'https://skiing-time-about-us.streamlit.app/'
      sl.markdown(f'[About us]({about_us_page_url})')
   
   with column[4]:
      github_url = 'https://github.com/AlexTraveling/skiing_time_deploy'
      sl.markdown(f'[GitHub]({github_url})')


# Title Section
def title_section():

   sl.markdown('''

   <br>

   <h1 class="title">
      A Faster Way to Search Your Amazing Skiing Photos
   </h1>

   <br>

   <p class="describe">
      Skiing Time app offers AI Searching to make photo selecting more convenient
   </p>

   <br>
               
   <style>

   .title {
      text-align: center;
   }
   .describe {
      text-align: center;
      color: grey;
   }

   </style>

   ''', unsafe_allow_html=True)


# Goto Use Section
def goto_use_section():

   sl.markdown('''
               
   <style>

   .st-emotion-cache-7ym5gk.ef3psqc12 {
      width: 80%;
      margin-left: 10%;
      # background: rgb(255, 75, 75);
      # border: 0px;
      # color: white;
   }

   </style>

   ''', unsafe_allow_html=True)

   if_goto_login = sl.button('Try Skiing Time Now')

   if if_goto_login:

      information = f'nothing'

      subprocess.Popen(["streamlit", 
                        "run", 
                        "login_page.py", 
                        "information", 
                        f"{information}"])
   

# Demonstration Video Section
def demonstration_section():

   sl.markdown('''
               
   <br>
               
   <style>

   .stVideo {
      border-radius: 10px;
      autoplay: true;
   }

   </style>

   ''', unsafe_allow_html=True)

   demonstration_video_path = 'home_page_material/marvelous_demo_vlog.m4v'
   sl.video(demonstration_video_path)


# Help in home page Section
def help_section():
   sl.markdown('''


   <h1 class="title">
      Easier than Easier to Use
   </h1>

   <br>

   <p class="describe">
      Just three steps to use Ai Searching of Skiing Time
   </p>

   <br>
               
   <style>

   .title {
      text-align: center;
   }
   .describe {
      text-align: center;
      color: grey;
   }

   </style>

   ''', unsafe_allow_html=True)

   step_1()
   step_2()
   step_3()


# Information Section
def information():

   sl.markdown('---')

   column = sl.columns([0.2, 1, 1, 1, 1])

   with column[1]:
      sl.subheader('SITE')
      sl.caption('Home')
      sl.caption('Sign up')
      sl.caption('Log in')
      sl.caption('Gallery of photos')
      sl.caption('AI searching')
      sl.caption('Download')
      
   with column[2]:
      sl.subheader('TECH')
      sl.caption('Streamlit')
      sl.caption('Python 3')
      sl.caption('My SQL')
      sl.caption('CLIP model')
   
   with column[3]:
      sl.subheader('TEAM')
      sl.caption('Alex Zhao')
      sl.caption('Zhengyi Guo')
      sl.caption('Zirui Chen')
      sl.caption('Wenhao Zhang')

   with column[4]:
      sl.subheader('SOCIAL')
      sl.caption('GitHub')
      sl.caption('CAU')
      sl.caption('Easthome')
      sl.caption('滑呗')
      sl.caption('GOSKI')
   

# Bottom Section
def bottom_section():

   sl.markdown('---')

   column = sl.columns([3, 2, 3])
   with column[1]:
      logo_path = 'home_page_material/skiing_time_logo_2.png'
      sl.image(logo_path)

   # sl.text('a web app for AI searching')
   sl.markdown('''

   <p class="bottom">
      a web app for AI searching of skiing photos developed by team Skiing Time of CAU
   </p>
   <p class="bottom">
      March 2024, Peking City
   </p>
      

   <br>
               
   <style>

   .title {
      text-align: center;
   }
   .bottom {
      text-align: center;
      color: lightgrey;
   }

   </style>

   ''', unsafe_allow_html=True)

   pass


# Home Page
def home_page():

   top_section()
   title_section()
   goto_use_section()
   demonstration_section()
   sl.markdown('---')
   help_section()
   information()
   bottom_section()


if __name__ == '__main__':

   home_page()