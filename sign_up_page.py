import streamlit as sl
import time
import subprocess

from userDatabase import if_exist
from userDatabase import add_user


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

   sl.markdown('<h1 class="title">Sign Up</h1>', unsafe_allow_html=True)
   
   sl.markdown('<p class="direction">Username and password are required for a new account</p>', unsafe_allow_html=True)


def account_section():

   with sl.form('sign_up'):
      username = sl.text_input('New username')
      password = sl.text_input('New password', type='password', key='first_password')
      check_password = sl.text_input('Confirm password', type='password', key='second_password')

      sl.markdown('''
      <style>       
      .st-emotion-cache-7ym5gk.ef3psqc7 {
         width: 100%;
      }         
      <style>
      ''', unsafe_allow_html=True)

      if sl.form_submit_button('Sign up'):

         if username == '':
            sl.warning('Username empty')
         elif password == '':
            sl.warning('Password empty')
         elif check_password == '':
            sl.warning('Please confirm password')

         else:
            if password != check_password:
               sl.warning('Passwords are not same')

            else:
               if if_exist(username):
                  sl.warning('Username already existed')
               else:

                  add_user(username, password)
                  sl.success('Sign up successfully')
                  return True, username, password
   
   return False, None, None


def goto_login_section():

   sl.markdown('''
   <style>
   .st-emotion-cache-1umgz6k.ef3psqc12 {
      border-color: transparent;
      color: gray;
   }
   </style>''', unsafe_allow_html=True)

   col1, col2, col3 = sl.columns([1, 2, 1])
   with col2:
      sign_up_button = sl.button('Back to log in Skiing Time', use_container_width=100)

   if sign_up_button:
      sl.warning('Back to log in...')
      time.sleep(0.5)

      subprocess.Popen(["streamlit", 
                     "run", 
                     "login_page.py", 
                     "none", 
                     f"{404}"])
      

def sign_up_page():

   title_section()
   account_section()
   goto_login_section()
   

if __name__ == "__main__":

   sign_up_page()