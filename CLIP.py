import torch
from PIL import Image
from transformers import AutoProcessor, CLIPModel
import torch.nn as nn


def CLIP(double_image):
   
   a = double_image[0]
   b = double_image[1]

   # device = torch.device('cuda' if torch.cuda.is可用 else "cpu")
   device = torch.device('mps')

   processor = AutoProcessor.from_pretrained("openai/clip-vit-base-patch32")
   model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
   
   # Extract features from image1
   # image1 = Image.open(f'/Users/zxb/Documents/CAU/GradeFour/实习/2-streamlit_practice/my_images/image_{a}.jpg')
   image1 = a
   with torch.no_grad():
      inputs1 = processor(images=image1, return_tensors="pt").to(device)
      image_features1 = model.get_image_features(**inputs1)
   
   # Extract features from image2
   # image2 = Image.open(f'/Users/zxb/Documents/CAU/GradeFour/实习/2-streamlit_practice/my_images/image_{b}.jpg')
   image2 = b
   with torch.no_grad():
      inputs2 = processor(images=image2, return_tensors="pt").to(device)
      image_features2 = model.get_image_features(**inputs2)
   
   # Compute their cosine similarity and convert it into a score between 0 and 1
   cos = nn.CosineSimilarity(dim=0)
   sim = cos(image_features1[0],image_features2[0]).item()
   sim = (sim+1)/2

   print('done.')

   return sim


if __name__ == "__main__":

   sim = CLIP(2.1, 2)
   print('Similarity:', sim)

