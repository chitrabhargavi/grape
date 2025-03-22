
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
