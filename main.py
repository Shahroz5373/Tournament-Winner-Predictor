import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\YourUsername\Documents\BigDataProject\pslData.csv')

team_encoder = LabelEncoder()

df['Team1'] = team_encoder.fit_transform(df['Team1'])
df['Team2'] = team_encoder.transform(df['Team2'])
df['Team3'] = team_encoder.transform(df['Team3'])
df['Team4'] = team_encoder.transform(df['Team4'])

x = df[['Year', 'Team1', 'Team2', 'Team3', 'Team4']]
y = df['Winner']

winner_encoder = LabelEncoder()
y = winner_encoder.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

model = LinearRegression()
model.fit(x_train, y_train)

def predict_winner(year, team1, team2, team3, team4):
    team1_encoded = team_encoder.transform([team1])[0]
    team2_encoded = team_encoder.transform([team2])[0]
    team3_encoded = team_encoder.transform([team3])[0]
    team4_encoded = team_encoder.transform([team4])[0]
    
    
    input_data = np.array([[year, team1_encoded, team2_encoded, team3_encoded, team4_encoded]])
    
    
    predicted_winner = model.predict(input_data)
    
    
    predicted_winner_team = winner_encoder.inverse_transform([int(predicted_winner.round().item())])[0]
    
    return predicted_winner_team

def plot_total_wins():
    
    decoded_winners = winner_encoder.inverse_transform(y)
    
    
    wins_df = pd.DataFrame(decoded_winners, columns=['Winner'])
    
    
    win_counts = wins_df['Winner'].value_counts()
    
    
    plt.figure(figsize=(10, 6))
    win_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title('Total Wins by Team in the Tournament')
    plt.ylabel('')  
    plt.show()


year = int(input("Enter the year: "))
team1 = input("Enter Team 1: ")
team2 = input("Enter Team 2: ")
team3 = input("Enter Team 3: ")
team4 = input("Enter Team 4: ")


winner = predict_winner(year, team1, team2, team3, team4)
print(f"The predicted winner for the year {year} is: {winner}")


plot_total_wins()
