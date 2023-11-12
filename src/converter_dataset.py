# PARA EN CASO DEL ENTRENAMIENTO SEA AQUI
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import shutil

# Rutas de los archivos y carpetas
csv_path = './src/dataset/stage_2_train_labels.csv'
images_folder = './src/dataset/stage_2_train_images'
output_folder = './src/data_dcm'

# Crear carpetas para train, test y valid
for folder in ['train', 'test', 'valid']:
    os.makedirs(os.path.join(output_folder, folder, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, folder, 'labels'), exist_ok=True)


df = pd.read_csv(csv_path)
df = df.fillna(0.0)

# 70% train , 15% train , 15% valid
# Dividir en entrenamiento (70%) y test + validación (30%)
train_df, test_valid_df = train_test_split(df, test_size=0.3, random_state=42)
# Dividir test + validación en test (15%) y validación (15%)
test_df, valid_df = train_test_split(test_valid_df, test_size=0.5, random_state=42)


# Crear etiquetas yolo
def copy_images_and_labels(df, output_folder):
    for index, row in df.iterrows():
        image_id = row['patientId']
        target = row['Target']
        
        # Copiamos la imagen
        src_image_path = os.path.normpath(os.path.join(images_folder, f'{image_id}.dcm'))
        dst_image_path = os.path.normpath(os.path.join(output_folder, 'images', f'{image_id}.dcm'))
        shutil.copy(src_image_path, dst_image_path)

        label_file_path = os.path.normpath(os.path.join(output_folder, 'labels', f'{image_id}.txt'))
        #print(f"SH: {label_file_path}")

        if os.path.exists(label_file_path):
            mode = 'a'  # Agregar existente
        else:
            mode = 'w'  

        label_file_save = os.path.normpath(os.path.join(output_folder, 'labels', f'{image_id}.txt'))
        #print(f"SV: {label_file_save}")
        with open(label_file_save, mode) as label_file:  
            label_file.write(f'{target} {row["x"]} {row["y"]} {row["width"]} {row["height"]}\n')


def convert_dataset_to_yolo():
    print("... Iniciando segmentación YOLO V5 ...")
   
    print("... Data TRAIN ...")
    copy_images_and_labels(train_df, os.path.join(output_folder, 'train'))    
    print("... Data TRAIN termined ...")

    print("... Data TEST ...")
    copy_images_and_labels(test_df, os.path.join(output_folder, 'test')) 
    print("... Data TEST termined ...")

    print("... Data VALID ...")
    copy_images_and_labels(valid_df, os.path.join(output_folder, 'valid'))
    print("... Data VALID termined...")
