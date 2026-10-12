# ML-Based Software Design Pattern Detection Using Neural Networks

## 📌 Project Overview

This project focuses on detecting software design patterns in source code using Machine Learning and Artificial Neural Networks (ANN). It aims to analyze source code, process relevant features, and classify design patterns to help developers understand the structure and design of software applications.

## 🎯 Objectives

- Automate the detection of software design patterns from source code.
- Apply machine learning and neural network techniques for classification.
- Preprocess source code and extract meaningful features.
- Evaluate model performance using suitable evaluation metrics.
- Provide a simple interface for interacting with the prediction system.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Artificial Neural Network (ANN)
- **Deep Learning Framework:** TensorFlow, Keras
- **Text Processing:** NLTK
- **Feature Extraction:** TF-IDF
- **Data Processing:** NumPy, Pandas
- **Interface:** Tkinter

## ⚙️ Project Workflow

1. **Source Code Input:** Provide source code for analysis.
2. **Preprocessing:** Clean and prepare the source code for analysis.
3. **Feature Extraction:** Convert text/code into numerical features using TF-IDF.
4. **Model Prediction:** Use the trained neural network to classify the input.
5. **Result Display:** Display the prediction through the application interface.

## 📂 Project Structure

```text
DesignPatternFiles/
├── designpatternprediction.py
├── requirements.txt
├── sitecustomize.py
└── model/
    ├── features.csv
    ├── vector.txt
    ├── model_weights.hdf5
    └── history.pckl
```

**Note:** The `model/` directory contains supporting model files. The exact files should match your project folder.

## 💻 Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd DesignPatternFiles
```

### 2. Create a virtual environment

```bash
py -3.11 -m venv .venv311
```

### 3. Activate the environment (Windows PowerShell)

```powershell
.\.venv311\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Make sure the installed package versions are compatible with Python 3.11 and with the project's existing code.

### 5. Download NLTK stopwords

```bash
python -c "import nltk; nltk.download('stopwords')"
```

### 6. Run the application

If you are using the compatibility file `sitecustomize.py` created for the legacy Keras import, run:

```powershell
python -c "import sitecustomize; import runpy; runpy.run_path('designpatternprediction.py', run_name='__main__')"
```

## 📊 Model Evaluation

The project can use the following metrics to assess classification performance:

- Accuracy
- Precision
- Recall
- F1-score

Actual performance values depend on the trained model and evaluation dataset.

## ✨ Key Features

- Automated software design pattern prediction.
- Source code preprocessing and feature extraction.
- Neural-network-based classification.
- Graphical user interface for user interaction.
- Reusable trained model and feature-processing files.

## 🔮 Future Enhancements

- Support for additional software design patterns.
- Improve model accuracy with larger and more diverse datasets.
- Add support for more programming languages.
- Develop a web-based interface.
- Integrate code analysis and visualization features.

## 👨‍💻 Author

**Jannu Venkata Ayyappa**

Artificial Intelligence and Machine Learning Student

DVR & Dr. HS MIC College of Technology

## 📄 License

Add a suitable open-source license if you intend to allow others to reuse, modify, or distribute this project.
