# 🔋 Battery Wear Level Predictor

This project uses a K-Nearest Neighbors (KNN) regression model to predict battery wear levels based on age and charge cycle frequency.

## 📊 Dataset
- **Features**:
  - `Battery Age (Years)`
  - `Charge Cycle/24hrs`
- **Target**:
  - `Battery Wear Level (%)`

## 🧠 ML Model
- Algorithm: `KNeighborsRegressor` (from Scikit-learn)
- Preprocessing: Feature scaling
- Metrics: Mean Squared Error (MSE)

## ⚙️ How to Use
1. Run `BatteryWearLevelPredictors.py`.
2. Enter battery age and daily charge cycles when prompted.
3. Get the predicted battery wear level.

## 🧪 Sample Output

