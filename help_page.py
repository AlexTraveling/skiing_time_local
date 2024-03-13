import streamlit as sl
import streamlit.components.v1 as com


# Title section
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

   sl.markdown('<h1 class="title">Only Take Three Steps</h1>', unsafe_allow_html=True)
   sl.markdown('<h4 class="direction">learn how to select your photos by AI searching</h4>', unsafe_allow_html=True)
   sl.markdown('---')
   

# Step 1: Time and resort
def step_1():

   column = sl.columns([2, 3])
   
   with column[0]:
      sl.title('Choose Date and Resort')
      sl.write('Enjoy all photos after choosing specific date and resort in Gallery Page. Then you may click button of Go Ai Searching to use it.')

   with column[1]:
      sl.image('help_page_material/gallery.png')


# Step 2: Upload one photo
def step_2():

   column = sl.columns([2, 3])
   
   with column[0]:
      sl.title('Upload One Old Photo')
      sl.write('System can analyze which part of photos belong to you automatically by the marvelous CLIP deep learning model.')

   with column[1]:
      sl.image('help_page_material/upload_2.png')


# Step 3: Select and download photo after AI searching
def step_3():

   column = sl.columns([2, 3])
   
   with column[0]:
      sl.title('Download Your Checked Photos')
      sl.write('Take the further selection after AI searching and download all photos.')
      sl.write('You may also use the Threshold Slider to adjust threshold inside CLIP deep learning model. Upper brings better accuracy and lower brings better completness.')

   with column[1]:
      sl.image('help_page_material/download.png')


# Help page
def help_page():

   page_name = 'Help · Skiing Time'
   page_icon = '🏂'
   sl.set_page_config(page_name, page_icon)

   title_section()
   step_1()
   sl.markdown('---')
   step_2()
   sl.markdown('---')
   step_3()


if __name__ == '__main__':

   help_page()