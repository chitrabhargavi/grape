
# 🍇 Grape Leaf Detection Using Image Processing  

This project detects and classifies grape leaves using image processing and machine learning techniques. It extracts shape, color, and texture features from images and applies multiple classifiers to predict the leaf type or disease.  

## 📌 Features  
- **Feature Extraction**: Computes shape descriptors, color statistics, and texture properties.  
- **Dataset Processing**: Reads images from a dataset, extracts features, and saves them to a CSV file.  
- **Machine Learning Models**: Trains classifiers (SVM, Random Forest, Decision Tree, AdaBoost, Bagging) for prediction.  
- **GUI Interface**: Provides an easy-to-use interface for dataset loading, training, and prediction.  

## 🛠 Technologies Used  
- Python  
- OpenCV  
- NumPy, Pandas  
- scikit-learn  
- Tkinter (GUI)  
- Matplotlib, Seaborn  

## 📂 Project Structure  
```
📦 GrapeLeafDetection
 ┣ 📜 feature_extract.py  # Extracts image features
 ┣ 📜 train.py            # Processes dataset and saves extracted features
 ┣ 📜 final.py            # GUI & ML model training
 ┗ 📜 README.md           # Project documentation
```

## 🔧 Installation  
Ensure you have Python 3.x installed. Install dependencies using:  
```bash
pip install numpy opencv-python pandas scikit-learn matplotlib seaborn imutils
```

## 🚀 Usage  

### 1️⃣ Extract Features  
```python
from feature_extract import featureExtraction
features = featureExtraction("sample.jpg", show=True)
print(features)
```

### 2️⃣ Process Dataset & Save Features  
Run `train.py` to extract features from images and save them:  
```bash
python train.py
```

### 3️⃣ Train & Test ML Models  
Run the GUI using:  
```bash
python final.py
```
- Upload dataset (`grape_features.csv`)  
- Train models  
- Predict leaf type using an image  

## 📊 Machine Learning Models  
The project evaluates different classifiers:  
- **SVM (Linear)**  
- **Random Forest**  
- **Decision Tree**  
- **AdaBoost**  
- **Bagging Classifier**  

### 📈 Model Performance  
Once trained, the models’ performance can be compared using a bar graph.

## 📌 Example Prediction  
After training, select an image to predict its class:  
```python
test.pred()
```
## screenshots
![image](https://github.com/user-attachments/assets/10c898ee-c0b9-4caa-8a2a-3c93f3951a7a)
![image](https://github.com/user-attachments/assets/41586b26-95bd-4f73-99ec-1335fae2c8f9)
![image](https://github.com/user-attachments/assets/f624a093-7f7d-44fb-a467-fb95d376cf29)
![image](https://github.com/user-attachments/assets/5c429505-12bc-4896-9142-ea5cdfa3cef4)
![image](https://github.com/user-attachments/assets/09f4737a-1bb8-4e21-9a8a-a8a2c13205c3)
![image](https://github.com/user-attachments/assets/ee80c88b-93bb-46b6-a493-54f79d7ca6c9)
![image](https://github.com/user-attachments/assets/0530e7fc-e3d0-46de-b5d1-baf7a78a8c87)
![image](https://github.com/user-attachments/assets/afb9474d-2e44-4945-91ed-250f9aaa6dff)
![image](https://github.com/user-attachments/assets/9eb0c6c6-72d9-4599-a625-5dad8fc989ce)
![image](https://github.com/user-attachments/assets/8d955dea-f717-4efe-b40a-389c6b169aaa)
![image](https://github.com/user-attachments/assets/7fce97d7-a0aa-48a9-9d59-a5b0542e6880)
![image](https://github.com/user-attachments/assets/19f8807a-090e-4953-92e5-c60e5a59efdc)
![image](https://github.com/user-attachments/assets/b9b9b90f-45cc-4723-a6c8-e269de72d7b8)
![image](https://github.com/user-attachments/assets/ee16b306-0b7a-42b8-bcee-3d43807e8c86)

