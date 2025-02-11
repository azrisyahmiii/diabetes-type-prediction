# Diabetes Prediction using Machine Learning

This project aims to predict the type of diabetes a patient may have using machine learning models. The dataset contains various medical parameters, and the models are trained to classify different types of diabetes.

## Project Overview

- **Exploratory Data Analysis (EDA)**: Conducted in `main.ipynb` to clean, analyze, and visualize data.
- **Feature Selection & Model Training**: Implemented using various machine learning classifiers.
- **Diabetes Prediction Web App**: A Streamlit-based web application (`app.py`) for user interaction and prediction.

## Dataset

The dataset consists of **70,000** instances with **34** attributes. The target variable is the type of diabetes diagnosed.

**Dataset Source:** The dataset is obtained from Kaggle: [Diabetes Dataset](https://www.kaggle.com/datasets/ankitbatra1210/diabetes-dataset/data)

## Running the Project

### 1. Perform Data Analysis & Model Training

Run the Jupyter Notebook `main.ipynb` to:
- Load and preprocess the dataset
- Perform feature selection using Boruta
- Train multiple models (Logistic Regression, Decision Tree, SVM, Random Forest, Gradient Boosting, XGBoost, etc.)
- Evaluate model performance

### 2. Run the Diabetes Prediction Web App

To launch the web application:

```bash
streamlit run app.py
```

This will start a local Streamlit server, and you can interact with the app in your browser.

## Model Details

- **Random Forest** is used as the predictive model for the app as it is the best-performing model
- The model is stored in `saved_models/Random Forest.pkl` along with:
  - `scaler.pkl` (for feature scaling)
  - `target_encoder.pkl` (for label encoding)
  - `selected_features.pkl` (features used for prediction)
- **Changing the Model**: You can change the model used in `app.py` by modifying the following line:
  ```python
  best_model_name = "Random Forest.pkl" # can be changed to any model
  ```
  Replace it with the name of another `.pkl` model available in the `saved_models/` directory.
  
## Project Structure

```
├── saved_models/         # Trained model and preprocessing tools
│   ├── Decision Tree.pkl
│   ├── Gradient Boosting.pkl
│   ├── K-Nearest Neighbors.pkl
│   ├── Logistic Regression.pkl
│   ├── Naive Bayes.pkl
│   ├── Random Forest.pkl
│   ├── Support Vector Machine.pkl
│   ├── XGBoost.pkl
│   ├── scaler.pkl
│   ├── label_encoders.pkl
│   ├── target_encoder.pkl
│   ├── selected_features.pkl
├── app.py                # Streamlit Web App
├── main.ipynb            # Data Analysis & Model Training Notebook
├── diabetes_dataset00.csv  # Dataset
└── README.md
```

Developed as part of a Data Mining project for **CDS6314 Data Mining** under Multimedia University Cyberjaya.
