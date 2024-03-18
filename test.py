import os
import torch
path = './dataset/plant-seedlings-classification.zip'
data_dir = os.path.exists(path)
print(data_dir)
print(torch.__version__)
print(torch.cuda.is_available())