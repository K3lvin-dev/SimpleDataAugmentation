# importar os pacotes necessários
import numpy as np
import os
from PIL import Image
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.preprocessing.img import ImageDataGenerator
import shutil

# Verifica os diretorios
if not os.path.exists('mid'):
    os.makedirs('mid')
else:
    shutil.rmtree('mid')
    os.makedirs('mid')

if not os.path.exists('output'):
    os.makedirs('output')
else:
    shutil.rmtree('output')
    os.makedirs('output')

# Data augmentation
for i in range(1, 7, 1):
    os.mkdir(f'./mid/{i}')
    for h in range(1, 101, 1):
        IMAGE_PATH = f'Fotos/pessoa.{i}.{h}.jpg'
        OUTPUT_PATH = f'./mid/{i}'

        # carregar a imagem original e converter em array
        img = load_img(IMAGE_PATH)
        img = img_to_array(img)

        # adicionar uma dimensão extra no array
        img = np.expand_dims(img, axis=0)

        # criar um gerador (generator) com as imagens do data augmentation
        imgAug = ImageDataGenerator(rotation_range=45, width_shift_range=0.1,
                                    height_shift_range=0.1, horizontal_flip=True)

        imgGen = imgAug.flow(img, save_to_dir=OUTPUT_PATH,
                             save_format='jpg', save_prefix=f'pessoa.{i}.{h}')

        # gerar 10 imagens por data augmentation
        counter = 0

        for (z, newImage) in enumerate(imgGen):
            counter += 1
            # ao gerar 10 imagens, parar o loop
            if counter == 3:
                break

for z in range(1, 7, 1):
    path = f'./mid/{z}/'
    files = os.listdir(path)
    # Renomeia as Fotos
    for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, f'pessoa.{z}.{index}.jpg'))
        im = Image.open(f'./mid/{z}/pessoa.{z}.{index}.jpg')
        # Converte para png 8 bit
        im.convert('L').save(f'./output/pessoa.{z}.{index}.png')

shutil.rmtree('mid')
