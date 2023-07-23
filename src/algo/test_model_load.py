import pickle
import pandas as pd

import os

model_file = os.path.join("src", "algo", "model.pickle")

with open(model_file, "rb") as f:
    model = pickle.load(f)


sample_data = pd.DataFrame(
    {
        "Martin Brundle": {
            "Race_Entries": 165.0,
            "Race_Starts": 158.0,
            "Pole_Positions": 0.0,
            "Race_Wins": 0.0,
            "Fastest_Laps": 0.0,
        },
        "Niki Lauda": {
            "Race_Entries": 177.0,
            "Race_Starts": 171.0,
            "Pole_Positions": 24.0,
            "Race_Wins": 25.0,
            "Fastest_Laps": 24.0,
        },
        "Graham Hill": {
            "Race_Entries": 179.0,
            "Race_Starts": 176.0,
            "Pole_Positions": 13.0,
            "Race_Wins": 14.0,
            "Fastest_Laps": 10.0,
        },
        "Valtteri Bottas": {
            "Race_Entries": 202.0,
            "Race_Starts": 201.0,
            "Pole_Positions": 20.0,
            "Race_Wins": 10.0,
            "Fastest_Laps": 19.0,
        },
        "Giancarlo Fisichella": {
            "Race_Entries": 231.0,
            "Race_Starts": 229.0,
            "Pole_Positions": 4.0,
            "Race_Wins": 3.0,
            "Fastest_Laps": 2.0,
        },
        "Lewis Hamilton": {
            "Race_Entries": 311.0,
            "Race_Starts": 311.0,
            "Pole_Positions": 103.0,
            "Race_Wins": 103.0,
            "Fastest_Laps": 61.0,
        },
    }
)
input_data = sample_data.T
input_data.loc[:, "Races_to_Wins"] = (
    input_data["Race_Wins"] / input_data["Race_Entries"]
)
input_data.loc[:, "Races_to_Poles"] = (
    input_data["Pole_Positions"] / input_data["Race_Entries"]
)
input_data = input_data.drop(
    columns=["Race_Wins", "Race_Entries", "Pole_Positions"]
)

print(f"Input data shape: {input_data.shape}")
print(
    "Predictions:"
    f" {[f'{driver}: {champion}' for driver, champion in zip(input_data.index, model.predict(input_data))]}"
)
