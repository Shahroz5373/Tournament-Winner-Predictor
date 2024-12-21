# Tournament Winner Predictor

This project predicts the winner of the Pakistan Super League (PSL) tournament based on historical data. By analyzing the semifinalist teams and the winner from previous years, the program can predict the winner for a given set of semifinalist teams for an upcoming year.

## Features
- **Prediction Model**: Uses machine learning to predict the tournament winner.
- **Data Encoding**: Encodes team names and winner data for accurate model training.
- **Visualization**: Provides a pie chart showing total wins by teams across all years in the dataset.

## Technologies Used
- **Python**: Core programming language for this project.
- **Pandas**: For data manipulation and preprocessing.
- **Scikit-learn**: For building and training the prediction model.
- **Matplotlib**: For visualizing team win statistics.

## Dataset
The dataset used is `pslData.csv`, which includes the following columns:
- `Year`: The year of the tournament.
- `Team1`, `Team2`, `Team3`, `Team4`: The semifinalist teams.
- `Winner`: The winner of the tournament.

## How It Works
1. **Data Preprocessing**:
   - Team names and winners are encoded using `LabelEncoder`.
   - The dataset is split into training and testing sets.
2. **Model Training**:
   - A machine learning model (default: Linear Regression) is trained on the historical data.
3. **Prediction**:
   - Given a year and the names of four semifinalist teams, the model predicts the winner.
4. **Visualization**:
   - A pie chart visualizes the total wins by each team in the dataset.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Shahroz5373/Tournament-Winner-Predictor.git
   ```
   Or [download it here](https://github.com/Shahroz5373/Tournament-Winner-Predictor/archive/refs/heads/main.zip).

2. Navigate to the project directory:
   ```bash
   cd Tournament-Winner-Predictor
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. Enter the year and the names of four semifinalist teams when prompted.
3. View the predicted winner and optionally display the pie chart of total wins.

## Example
```text
Enter the year: 2025
Enter Team 1: Lahore Qalandars
Enter Team 2: Multan Sultans
Enter Team 3: Karachi Kings
Enter Team 4: Islamabad United
The predicts winner for the year 
```

## Future Enhancements
- Switch to a classification model for improved prediction accuracy.
- Integrate the project into an Android app using Chaquopy for cross-language functionality.
- Expand the dataset to include additional years and tournaments.



## Contributions
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
