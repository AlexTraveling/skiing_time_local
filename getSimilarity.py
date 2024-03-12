import multiprocessing
from PIL import Image
import time

from CLIP import CLIP


def get_data():

   image_sum = 10
   image_list = []
   CLIP_data_list = []

   for i in range(0, image_sum):

      image_path = f'/Users/zxb/Documents/CAU/GradeFour/实习/2-streamlit_practice/images/photo-{i}.jpg'
      image_list.append(Image.open(image_path))
      upload_image = Image.open('/Users/zxb/Documents/CAU/GradeFour/实习/2-streamlit_practice/images/photo-0.jpg')
      CLIP_data_list.append((Image.open(image_path), upload_image))
   
   return image_list, CLIP_data_list


# def normal():

   t1 = time.time()

   image_list = get_data()[0]
   print(len(image_list))
   # print(image_list)

   similarity_list = []

   for i in range(len(image_list)):
      s = CLIP((image_list[i], image_list[0]))
      print(f'【{i}】{s}')
      similarity_list.append(s)

   t2 = time.time()

   print(f'Cost time: {t2 - t1}')

   return similarity_list


def get_similarity_by_pool(data_list):

   t1 = time.time()

   cpu_core_quantity = 6
   pool = multiprocessing.Pool(cpu_core_quantity)
   similarity_list = pool.map(CLIP, data_list)

   pool.close()
   pool.join()

   for i in range(len(similarity_list)):
      print(f'【{i}】{similarity_list[i]}')

   t2 = time.time()
   cost_time = t2 - t1
   print(f'Cost time: {cost_time}')

   return similarity_list, cost_time


if __name__ == "__main__":

   # normal()

   # print(multiprocessing.cpu_count())

   data_list = get_data()[1]
   print(len(data_list))
   # print(data_list)

   get_similarity_by_pool(data_list)


