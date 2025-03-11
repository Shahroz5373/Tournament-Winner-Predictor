# 🏆 Tournament Winner Predictor

This project is designed to predict the winner of the Pakistan Super League (PSL) based on historical tournament data. By analyzing past semifinalists and winners, the model forecasts the champion from a given set of semifinalist teams for an upcoming season.

---

## 🔥 Key Features
- **Intelligent Prediction**: Leverages machine learning to forecast tournament winners.
- **Data Encoding & Preprocessing**: Converts team names and results into a structured format for accurate predictions.
- **Statistical Visualization**: Generates pie charts showcasing total wins by each team.

---

## 🛠️ Technologies Used
- **Python**: Core programming language.
- **Pandas**: For handling and preprocessing historical PSL data.
- **Scikit-learn**: Implements machine learning for predictions.
- **Matplotlib**: Visualizes win distributions in a pie chart format.

---

## 📂 Dataset Overview
The dataset (`pslData.csv`) consists of the following columns:
- `Year`: The tournament year.
- `Team1`, `Team2`, `Team3`, `Team4`: The semifinalist teams.
- `Winner`: The champion team of that year.

---

## ⚙️ How It Works
1. **Preprocessing the Data**:
   - Team names and winners are encoded using `LabelEncoder`.
   - The dataset is split into training and testing subsets.
2. **Model Training**:
   - Uses a machine learning model (default: Linear Regression) to train on past tournament results.
3. **Making Predictions**:
   - Users input the year and four semifinalist teams, and the model predicts the most probable winner.
4. **Data Visualization**:
   - A pie chart displays the number of times each team has won the tournament.

---

## 🚀 Getting Started

### 📥 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Shahroz5373/Tournament-Winner-Predictor.git
   ```
   Or [download the ZIP file](https://github.com/Shahroz5373/Tournament-Winner-Predictor/archive/refs/heads/main.zip).

2. Navigate to the project directory:
   ```bash
   cd Tournament-Winner-Predictor
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### ▶️ Running the Project
1. Execute the script:
   ```bash
   python main.py
   ```
2. Enter the tournament year and four semifinalist teams when prompted.
3. View the predicted winner and an optional pie chart visualization of total wins.

---

## 🎯 Example Usage
```text
Enter the year: 2025
Enter Team 1: Lahore Qalandars
Enter Team 2: Multan Sultans
Enter Team 3: Karachi Kings
Enter Team 4: Islamabad United
Predicted Winner for 2025: Lahore Qalandars
```

---

## 🔮 Future Enhancements
- Transition to a classification model for higher prediction accuracy.
- Develop an Android app integrating this model using Chaquopy.
- Expand the dataset to include more seasons and international leagues.

---

## 👨‍💻 Collaborators

- **Meesum Afzaal**  
  🔗 [GitHub Profile](https://github.com/Meesum-Afzaal)  
  📧 [meesumafzal@gmail.com](mailto:meesumafzal@gmail.com)  

- **Muhammad Shahroz**  
  🔗 [GitHub Profile](https://github.com/Shahroz5373)  
  📧 [shahrozjavid5373@gmail.com](mailto:shahrozjavid5373@gmail.com)  

---

## 🤝 Contributions
We welcome contributions! Feel free to fork the repository, make improvements, and submit a pull request.

Happy coding! 🎉

