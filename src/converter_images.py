import os
import pydicom
from PIL import Image

def convert_dicom_to_jpg(input_dir, output_dir):
    # Obtén la lista de archivos DICOM en el directorio de entrada
    dicom_files = [f for f in os.listdir(input_dir) if f.endswith('.dcm')]

    # Crea el directorio de salida si no existe
    os.makedirs(output_dir, exist_ok=True)

    # Itera sobre cada archivo DICOM y convierte a JPEG
    for dicom_file in dicom_files:
        # Lee el archivo DICOM
        dicom_path = os.path.join(input_dir, dicom_file)
        dicom_data = pydicom.read_file(dicom_path)

        # Extrae la matriz de píxeles de la imagen DICOM
        pixel_array = dicom_data.pixel_array

        # Convierte la matriz de píxeles a una imagen Pillow
        image = Image.fromarray(pixel_array)

        # Crea la ruta de salida para el archivo JPEG
        output_path = os.path.join(output_dir, f'{dicom_file[:-4]}.jpg')

        # Guarda la imagen en formato JPEG
        image.save(output_path)

       

def convert_images():
    print("... Iniciando transformación de imagenes ...")
    
    print("... Data TRAIN ...")
    convert_dicom_to_jpg('./src/data_dcm/train/images', './src/data_jpg/train/images')
    print("... Data TRAIN termined ...")
    
    print("... Data TEST ...")
    convert_dicom_to_jpg('./src/data_dcm/test/images', './src/data_jpg/test/images')
    print("... Data TEST termined ...")

    print("... Data VALID ...")
    convert_dicom_to_jpg('./src/data_dcm/valid/images', './src/data_jpg/valid/images')
    print("... Data VALID termined ...")
