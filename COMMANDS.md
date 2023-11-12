```
!git clone https://github.com/ultralytics/yolov5  # clone repo  
%cd yolov5  
%      
%pip install -q roboflow  W
```  
```
!unzip -q /content/data.zip -d /content/
```

```
python train.py --img 640 --batch 4 --epochs 2 --data ./data/data.yaml --weights yolov5s.pt --cache
```  


## COMANDS IN GOOGLE COLAB  
```
!python train.py --img 640 --batch 4 --epochs 4 --data /content/yolov5/data/data.yaml --weights yolov5x.pt --cache
```  



## FINAL COMMAND  

```
python main.py // Este paso ya no, por que ya tenemos el dataset generado
//copiar los labels en cada archivo
cd src/yolov5
python train.py --img 640 --batch 4 --epochs 2 --data ./data/data1.yaml --weights yolov5s.pt --cache

```