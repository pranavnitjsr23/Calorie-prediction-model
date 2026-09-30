This project uses a machine learning model to predict the calories burned during exercise based on user inputs such as heart rate, exercise duration, weight, height, age, and body temperature.
 Features 
• User Inputs: Users can input personal details like age, height, weight, exercise duration, heart rate, and body temperature.
• Model: The project uses the XGBRegressor model to predict the calorie burn based on the provided input data. 
• Data Scaling: Data is standardized using StandardScaler to improve prediction accuracy.
• Visualization: Displays an image with a caption to illustrate the application. 
Data • Calories Data: The target data for calories burned, provided in calories.csv.
     • Exercise Data: The feature data for each exercise session, provided in exercise.csv.

1.Data Processing: Loads and scales exercise data. 
2.Model Training: Trains an XGBoost regression model on the provided data. 
3.Prediction: Predicts the calorie burn for the user's inputs. 
4.Display Results: Displays the predicted calories burned. 

Requirements
 • Python libraries: streamlit, pandas, numpy, scikit-learn, xgboost, PIL

The Dataset used for training the model in colab was taken from kaggle,the zip file consisted of 2 csv files. 
DATASET LINK : https://www.kaggle.com/datasets/fmendes/fmendesdat263xdemos/data

The Model Training Code can be accessed via Colab Link-: 
COLAB LINK : https://colab.research.google.com/drive/1jGfin_NBlQiKOnlEZPptPmkB8yKX5XlT?usp=sharing

1.TRAINING AND TESTING OF MODEL
A Brief about the steps followed : for training the model:
Import Libraries: Import essential Python libraries like pandas, numpy, scikit-learn, xgboost, and streamlit.
Data Loading: Load the calories.csv and exercise.csv files using pandas to get both the target (calories burned) and feature (exercise details) data.
Data Preprocessing: Merge Data: Merge the exercise and calories datasets based on the session or user ID for a complete dataset. Standardization: Use StandardScaler to scale features such as heart rate, age, weight, height, exercise duration, and body temperature, which improves model accuracy.
Model Selection and Training: Model Choice: Choose the XGBRegressor model, a gradient boosting model optimized for regression tasks. Train Model: Train the XGBRegressor on the preprocessed data, using calorie burn as the target variable.
Prediction: Collect user inputs for personal details and exercise metrics. Use the trained model to predict calories burned based on these inputs.

2. DEPLOYMENT 
Deployment of the model is done on Streamlit,for that on VS Code make a requirements.txt file and in the terminal run the following command 
' pip install -r requirements.txt ' .
After that for code you can refer to  ‘ Streamlit_Deployment.py .’  part of this repository.
Now to run streamlit in a browser run the following command in terminal:
‘ Streamlit run cpm.py ‘ (#streamlit run filename.py).

And Voila !,Your project is deployed successfully.




