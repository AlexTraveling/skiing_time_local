import streamlit as sl
import time
import subprocess

from userDatabase import get_user


# Get User Information Section
def user_account(username, password):

   save = get_user()
   
   if (username, password) in save:
      return True
   else:
      return False


# Title Section
def title_section():

   sl.markdown('''
   <style>
   .title {
      text-align: center;
   }
   .direction {
      text-align: center;
   }
   <style>
   ''', unsafe_allow_html=True)

   sl.markdown('<h1 class="title">Log in</h1>', unsafe_allow_html=True)
   sl.markdown('<p class="direction">Username and password are required to log in Skiing Time</p>', unsafe_allow_html=True)


# Log in Section
def login_section():

   with sl.form('login'):
      username = sl.text_input('Username')
      password = sl.text_input('Password', type='password')
      
      sl.markdown('''
      <style>       
      .st-emotion-cache-7ym5gk.ef3psqc7 {
         width: 100%;
      }         
      <style>
      ''', unsafe_allow_html=True)

      if_goto_gallery_button = sl.form_submit_button('Log in')

      if if_goto_gallery_button:
         if user_account(username, password):
            sl.success('Login successfully')
            time.sleep(2)
            return True, username
         else:
            sl.warning('Wrong username or password')
   
   return False, None


def goto_sign_up_section():

   sl.markdown('''
   <style>
   .st-emotion-cache-1umgz6k.ef3psqc12 {
      border-color: transparent;
      color: gray;
   }
   </style>''', unsafe_allow_html=True)

   col1, col2, col3 = sl.columns([1, 2, 1])
   with col2:
      sign_up_button = sl.button('Do not have a account ?  Sign up now', use_container_width=100)

   if sign_up_button:
      sl.warning('Ready to sign up...')
      time.sleep(0.5)

      subprocess.Popen(["streamlit", 
                     "run", 
                     "sign_up_page.py", 
                     "none", 
                     f"{404}"])


# Log in Page
def login_page():

   page_name = 'Log in · Skiing Time'
   page_icon = '🏂'
   sl.set_page_config(page_name, page_icon)

   title_section()
   if_goto_upload_page, username = login_section()
   goto_sign_up_section()

   if if_goto_upload_page == True:

      subprocess.Popen(["streamlit", 
                        "run", 
                        "gallery_page.py", 
                        "username", 
                        f"{username}"])


if __name__ == '__main__':

   login_page()