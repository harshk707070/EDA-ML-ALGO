# Insurance Charges Prediction

This repository contains a beginner-friendly project to predict medical insurance charges using a simple regression model. The process includes data analysis, cleaning, training a model, and visualizing predictions through a Streamlit app.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Model Training](#model-training)
- [Streamlit App (Optional)](#streamlit-app-optional)
- [Results](#results)

## Installation

To run the notebook locally, you need to have Python installed along with the necessary libraries. You can install the required libraries using `pip`.

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/repository-name.git
    cd repository-name
    ```

   2. Install the necessary libraries:
    ```bash
    pip install pandas numpy matplotlib seaborn plotly scikit-learn joblib streamlit jupyter
    ```

## Usage

You can either retrain the model from scratch using the provided cleaned dataset or directly run the interactive Streamlit app using the pre-trained files.

1. Launch Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
    
2. Open and run the EDA notebook:
    ```text
    eda_analysis.ipynb
    ```
    Performs cleaning, outlier removal, encoding, and saves the cleaned dataset as:
    ```bash
     data/cleaned_insurance.csv
    ```
    
3. Open and run the model training notebook:
  ```bash
  modeling.ipynb
  ```
  - Trains a RandomForestRegressor on the cleaned data
  - Saves two files:
      - models/random_forest_model.pkl — trained model
      - models/label_encoders.pkl — encoders for categorical features
OR

If you've already trained the model or want to use the pre-saved files:

  1. Navigate to the project folder:
    ```bash
    cd insurance-charges-prediction
    ```
  
  3. Run the Streamlit app:
    ```bash
    streamlit run streamlit_app.py
    ```

  4. The app will:
    - Take user inputs (age, sex, BMI, etc.)
    - Convert categorical inputs using label_encoders.pkl
    - Predict charges using random_forest_model.pkl
    - Display the predicted insurance cost in real time
    
## Dataset

The dataset used in this notebook is included in the repository.

## Linear Regression Model

The notebook demonstrates the following steps:

1. **Data Loading**: Load the dataset into a pandas DataFrame.
2. **Data Preprocessing**: Clean and preprocess the data for modeling.
3. **Model Training**: Train a linear regression model using scikit-learn.
4. **Model Evaluation**: Evaluate the model's performance using appropriate metrics.
5. **Visualization**: Visualize the results and the regression line.

### Results

The notebook includes visualizations of the dataset and the linear regression model. The performance metrics of the model are also displayed.

