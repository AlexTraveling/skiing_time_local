import streamlit as sl
import sys
from PIL import Image
import time

from getSimilarity import get_similarity_by_pool
from upload_page import new_get_data_list


# Get User Information Section
def user_information_section():

   index = sys.argv.index("from_upload_page")
   information = sys.argv[index + 1]

   cut = information.split("∆")

   username = cut[0]
   similarity_list = eval(cut[1])
   now_image_list = eval(cut[2])

   return username, similarity_list, now_image_list


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

   sl.markdown(f'<h1 class="title">We Have Found These for You, {username}</h1>', unsafe_allow_html=True)
   sl.markdown('<p class="direction">Upper for more accurate and lower for more abundant via threshold slider</p>', unsafe_allow_html=True)


# Set Threshold Section
def threshold_section():

   default_threshold = 0.90
   threshold = sl.slider('', 0.0, 1.0, default_threshold)

   return threshold


# Showcase and Tip Section
def get_upper_sum(similarity_list, threshold):

   sum = 0
   for s in similarity_list:
      if float(s) >= threshold:
         sum += 1

   return sum


def tip_section(similarity_list, threshold):

   image_sum = len(similarity_list)
   upper_sum = get_upper_sum(similarity_list, threshold)

   if upper_sum == 0:
      sl.warning(f'Here are {upper_sum} of the {image_sum} photos likely belong to you')
   else:
      sl.success(f'Here are {upper_sum} of the {image_sum} photos likely belong to you')

   time.sleep(0.2)
      

def showcase_section(upload_image, similarity_list, threshold, now_image_list):

   image_sum = len(similarity_list)
   image_list = new_get_data_list(upload_image, now_image_list)
   upper_list = []
   
   left, right = sl.columns(2)
   with left:
      for i in range(0, int(image_sum / 2)):
         if similarity_list[i] >= threshold:
            sl.image(image=image_list[i][0], use_column_width=True)
            sl.checkbox(f'Photo {now_image_list[i]} ({round(similarity_list[i], 3)})', key=f'checker{i}')
            upper_list.append(int(i))
   with right:
      for i in range(int(image_sum / 2), image_sum):
         if similarity_list[i] >= threshold:
            sl.image(image=image_list[i][0], use_column_width=True)
            sl.checkbox(f'Photo {now_image_list[i]} ({round(similarity_list[i], 3)})', key=f'checker{i}')
            upper_list.append(int(i))
   
   return image_sum, image_list, upper_list


# Download Button Section
def download_section(image_list, upper_list, now_image_list):

   sl.markdown('''
      <style>       
      .st-emotion-cache-7ym5gk.ef3psqc12 {
         width: 100%;
      }         
      <style>
      ''', unsafe_allow_html=True)

   download_button = sl.button('Download all checked photos')
   if download_button:
      for i in upper_list:
         if sl.session_state[f'checker{i}']:
            with sl.spinner(f"Photo {now_image_list[i]} is being downloaded"):
               image_list[i][0].save(f'download_image/save_photo_{now_image_list[i]}.png')
            sl.success(f"Download photo {now_image_list[i]} to local successfully")
   

# Download Page
def download_page():

   page_name = 'Download · Skiing Time'
   page_icon = '🏂'
   sl.set_page_config(page_name, page_icon)

   username, similarity_list, now_image_list = user_information_section()
   title_section(username)

   # default threshold = 0.95
   threshold = threshold_section()

   tip_section(similarity_list, threshold)
   upload_image = Image.open('upload_image/upload_image.png')
   image_sum, image_list, upper_list = showcase_section(upload_image, similarity_list, threshold, now_image_list)
   download_section(image_list, upper_list, now_image_list)


if __name__ == "__main__":

   download_page()