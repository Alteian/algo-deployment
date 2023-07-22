# Model prediction API
The goal of this task is to create API, which will predict whether given F1 race driver is a championship winner.  
The aim is to recreate possible flow in which Data Scientist with a model will come to you and ask you to serve a model in production.  
(this is just a part of the process, as this served model would still need to be consumed by other systems).

# Description
- `model.pickle` - The model. When given following attributes:
    ```
    'Race_Starts',
    'Fastest_Laps',
    'Races_to_Wins',
    'Races_to_Wins'
    ```
    It will predict whether given driver is a champion.
    Note that this model is quite bad, and often misclassifies the drivers.
- `training.ipynb` - This shows how the model was generated
- `test_model_load.py` - Shows how a given model could be opened and utilized.
- `data/F1_training.csv` - Training data. You can use them e.g. for testing purposes.

# Evaluation

We will send a request to your publicly available API with our holdout dataset.  
We expect that result from your API will match the result from the model trained before.

You are free to use cloud service of your own choice, but we prefer you to use AWS.
You are free to serve the API in any way you want but we expect you to provide us with documentation to given API.  
Document well how to call the API using Python.

In the end we will discuss the code and design choices together.

# Expected input (json)
```
{
    "Eddie Johnson": {
        "Race_Entries": 9.0,
        "Race_Starts": 9.0,
        "Pole_Positions": 0.0,
        "Race_Wins": 0.0,
        "Fastest_Laps": 0.0
    },
    "Paul Belmondo": {
        "Race_Entries": 27.0,
        "Race_Starts": 7.0,
        "Pole_Positions": 0.0,
        "Race_Wins": 0.0,
        "Fastest_Laps": 0.0
    },
    "Tarso Marques": {
        "Race_Entries": 26.0,
        "Race_Starts": 24.0,
        "Pole_Positions": 0.0,
        "Race_Wins": 0.0,
        "Fastest_Laps": 0.0
    },
    "Tom Bels\u00f8": {
        "Race_Entries": 5.0,
        "Race_Starts": 2.0,
        "Pole_Positions": 0.0,
        "Race_Wins": 0.0,
        "Fastest_Laps": 0.0
    }
}
```

# Expected output (json):
```
{
    "Eddie Johnson": 0,
    "Paul Belmondo": 0,
    "Tarso Marques": 0,
    "Tom Bels\u00f8": 0
}
```