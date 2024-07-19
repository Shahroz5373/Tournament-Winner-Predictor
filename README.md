# Tournament-Winner-Predictor
Big Data Project: Predicting Cricket Tournament Winners
Overview
This Python script demonstrates how to predict the winner of a cricket tournament using machine learning techniques. We’ll use a dataset containing historical match information to train a linear regression model. Additionally, we’ll visualize the total wins by each team in the tournament.

Steps:
Data Preparation:
Load the dataset from a CSV file (pslData.csv).
Encode team names using LabelEncoder.
Split the data into features (x) and the target variable (y).
Model Training:
Split the data into training and testing sets.
Train a LinearRegression model on the training data.
Prediction:
Input the year and team names for the upcoming tournament.
Encode team names and create an input array.
Predict the winner using the trained model.
Visualization:
Create a pie chart showing the distribution of total wins by each team.
Usage:
Run the script.
Enter the year and team names for the upcoming tournament.
The predicted winner will be displayed.
The pie chart will show the historical wins by each team.
Remember to replace the file path ('F:\\vs code files\\Big Data Project\\pslData.csv') with the actual path to your dataset
