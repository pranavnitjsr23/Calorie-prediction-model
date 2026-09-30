# Calorie Prediction Model

A machine learning regression project that predicts calories burned during exercise using demographic and exercise-related features.

## Overview

This project uses an XGBoost Regressor to estimate calories burned based on:

- Gender
- Age
- Height
- Weight
- Exercise Duration
- Heart Rate
- Body Temperature

The project follows an end-to-end machine learning workflow, including data preprocessing, exploratory data analysis, model training, cross-validation, hyperparameter tuning, and model evaluation. The final trained model is also deployed through a Streamlit web application.

## Dataset

The project uses two CSV files:

- `exercise.csv` — contains demographic and exercise-related features.
- `calories.csv` — contains the target variable, calories burned.

The datasets are joined using `User_ID`.

## Machine Learning Workflow

1. Load and inspect the datasets
2. Check for missing values and duplicates
3. Merge the datasets using `User_ID`
4. Encode the categorical `Gender` feature
5. Perform exploratory data analysis
6. Separate features and target variable
7. Split the data into training and testing sets
8. Train a baseline XGBoost regression model
9. Evaluate model performance using 5-fold cross-validation
10. Perform randomized hyperparameter tuning
11. Evaluate the tuned model on the held-out test set
12. Compare baseline and tuned model performance
13. Deploy the trained model using Streamlit

## Model

The project uses **XGBoost Regressor** for the regression task.

Hyperparameter tuning was performed using `RandomizedSearchCV` with 5-fold cross-validation. The search included parameters such as:

- `n_estimators`
- `max_depth`
- `learning_rate`
- `subsample`
- `colsample_bytree`

## Results

The tuned model was evaluated on the held-out test set.

| Metric | Baseline XGBoost | Tuned XGBoost |
|---|---:|---:|
| MAE | 1.498 | 0.938 |
| RMSE | 2.137 | 1.302 |
| R² | 0.99887 | 0.99958 |

The tuned model reduced MAE by approximately 37% and RMSE by approximately 39% compared with the baseline model.

## Streamlit Application

The trained model is deployed through a Streamlit application where users can enter their exercise details and receive a predicted calorie expenditure.

The application includes:

- Input validation
- Trained model loading
- Real-time prediction
- Basic error handling
- Interactive user interface

## Project Structure

```text
Calorie-Prediction-Model/
│
├── app.py
├── calorie_model.pkl
├── calories.csv
├── exercise.csv
├── burn.png
├── Calorie-prediction-model.ipynb
├── requirements.txt
└── .gitignore
```

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Streamlit
- Joblib
- Jupyter Notebook

## Running the Application

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in the browser at the local Streamlit address.

## Key Learning Outcomes

- Data preprocessing and exploratory data analysis
- Regression modeling with XGBoost
- Cross-validation
- Hyperparameter tuning
- Model evaluation using MAE, RMSE, and R²
- Model serialization using Joblib
- Deployment of a machine learning model using Streamlit
