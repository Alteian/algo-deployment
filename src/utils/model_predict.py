import typing
import pandas as pd
import pickle

from pathlib import Path


def model_predict_from_input(
    model: str, query_input: typing.Dict[str, typing.Dict[str, float]]
) -> typing.Dict[str, float]:
    with Path.open(model, "rb") as f:
        model = pickle.load(f)
    sample_data = pd.DataFrame(query_input)
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
    return {
        driver: float(champion)
        for driver, champion in zip(
            input_data.index, model.predict(input_data)
        )
    }
