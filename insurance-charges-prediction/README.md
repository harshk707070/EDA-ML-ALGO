# Insurance Charges Prediction

This repository contains a beginner-friendly project to predict medical insurance charges using a simple regression model. The process includes data analysis, cleaning, training a model, and visualizing predictions through a Streamlit app.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model](#model-training)
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

## Model

The modeling process is implemented in the notebook modeling.ipynb and follows these beginner-friendly steps:

1. Data Loading: Load the cleaned dataset (cleaned_insurance.csv) generated during EDA into a pandas DataFrame.

2. Encoding: Categorical columns like sex, smoker, and region are encoded using LabelEncoder for compatibility with scikit-learn models.

3. Model Training: A RandomForestRegressor is trained to predict insurance charges based on features like age, BMI, number of children, etc.

4. Saving the Model: After training, the following files are saved in the models/ directory:
    - random_forest_model.pkl: the trained Random Forest model.
    - label_encoders.pkl: encoders used to transform categorical inputs (needed during app inference).

5. Model Evaluation:
The model is evaluated using:

    Mean Absolute Error (MAE)
    Root Mean Squared Error (RMSE)
    R² Score (coefficient of determination)

These metrics give a sense of how accurately the model predicts insurance charges on unseen data.

### Results

Here are the Results for both EDA and the Model:

## EDA Results (Exploratory Data Analysis)

The initial dataset (`insurance.csv`) contained personal and health-related information for individuals along with their insurance charges. Here's what we discovered during EDA:

- **No Missing Values**:  
  There were no null values in any column. ✅

- **Categorical Columns Identified**:  
  `sex`, `smoker`, and `region` were identified as categorical columns to be encoded for modeling.

- **Age Groups**:  
  We added an `age_group` column to better understand trends across different age ranges, e.g., "18–25", "26–35", etc.

- **Outliers Detected**:  
  Some outliers were found in the `bmi` and `charges` columns using boxplots and were considered during visualization.

- **Visual Insights**:
  - Smokers have significantly higher insurance charges than non-smokers.
  - Charges tend to increase with age and BMI.
  - Males and females have similar distributions of charges.

- **Final Cleaned File**:  
  The cleaned dataset was saved as `cleaned_insurance.csv` in the `data/` folder and used for modeling.

## Results

After training a Random Forest Regressor on the cleaned data, we evaluated the model's performance using standard metrics:

- **Mean Absolute Error (MAE)**: ~2700 INR  
  → On average, the model's prediction is off by around ₹2700.

- **Root Mean Squared Error (RMSE)**: ~4300 INR  
  → A slightly more sensitive error measure. The higher it is, the more large errors exist.

- **R² Score**: ~0.88  
  → This means the model can explain about 88% of the variance in insurance charges — which is quite good!

These results suggest that the model is effective and suitable for real-world predictions, especially when used inside the Streamlit app for quick estimations.



