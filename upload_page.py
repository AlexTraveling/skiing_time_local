import streamlit as sl
import sys
import subprocess
from PIL import Image
import time
import datetime

from getSimilarity import get_similarity_by_pool
from gallery_page import select_section


# Get User Information Section
def user_information_section():

   information_index = sys.argv.index("information")
   information = sys.argv[information_index + 1]

   cut = information.split('∆')

   username = cut[0]
   date = cut[1]
   resort = cut[2]

   return username, date, resort


# Title Section
def title_section(username):

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

   sl.markdown(f'<h1 class="title">Hello {username}, Try the AI Searching</h1>', unsafe_allow_html=True)
   sl.markdown('<p class="direction">Upload your information and one photo to start AI searching</p>', unsafe_allow_html=True)


def new_get_data_list(upload_image, now_image_list):

   data_list = []

   for i in now_image_list:

      image_path = f'image_catalog/image_{i}.jpg'
      data_list.append((Image.open(image_path), upload_image))

   return data_list


def new_AI_search_section(upload_image, now_image_list):

   image_list = new_get_data_list(upload_image, now_image_list)

   with sl.spinner(f'All {len(image_list)} photos are being detected...'):
      similarity_list, cost_time = get_similarity_by_pool(image_list)

   sl.success(f'AI search successfully! time cost: {round(cost_time, 2)}s.')
   time.sleep(0.2)

   return similarity_list


def next_section(username, similarity_list, now_image_list):

   subprocess.Popen(["streamlit", 
                     "run", 
                     "download_page.py", 
                     "from_upload_page", 
                     f"{username}∆{similarity_list}∆{now_image_list}"])


def upload_section(username, default_date, default_resort):

   cut = default_date.split('-')
   year = int(cut[0])
   month = int(cut[1])
   day = int(cut[2])
   default_date = datetime.date(year, month, day)
   date = sl.date_input('Date', default_date)

   resort_list = ['Wanlong Holiday Paradise',
                  'Genting Yunding Garden',
                  'Thaiwood Ski Resort']
   default_index = resort_list.index(default_resort)
   resort = sl.radio('Resort', resort_list, default_index)

   # select section
   now_image_list = select_section(date, resort)

   # change here
   now_image_list = now_image_list[0]

   upload_file = sl.file_uploader('Upload photo', type=['jpg', 'png'])
   if upload_file is not None:
      sl.success('Upload successfully')
      time.sleep(0.5)
      sl.image(upload_file)

      sl.markdown('''
      <style>       
      .st-emotion-cache-7ym5gk.ef3psqc12 {
         width: 100%;
      }         
      <style>
      ''', unsafe_allow_html=True)

      if sl.button('Next'):

         if len(now_image_list) == 0:
            sl.error(f'There are no photo on {resort} on {date}')
         else:
            upload_image = Image.open(upload_file)
            upload_image.save('upload_image/upload_image.png')
            similarity_list = new_AI_search_section(upload_image, now_image_list)
            time.sleep(1)
            next_section(username, similarity_list, now_image_list)


# Upload Page
def upload_page():

   page_name = 'Upload · Skiing Time'
   page_icon = '🏂'
   sl.set_page_config(page_name, page_icon)

   username, default_date, default_resort = user_information_section()
   title_section(username)
   upload_section(username, default_date, default_resort)


if __name__ == "__main__":

   upload_page()