import httpx

STATUS_CODE_OK = 200

default_input_data = {
    "Eddie Johnson": {
        "Race_Entries": 9.0,
        "Race_Starts": 9.0,
        "Pole_Positions": 0.0,
        "Race_Wins": 0.0,
        "Fastest_Laps": 0.0,
    },
    "Paul Belmondo": {
        "Race_Entries": 27.0,
        "Race_Starts": 7.0,
        "Pole_Positions": 0.0,
        "Race_Wins": 0.0,
        "Fastest_Laps": 0.0,
    },
    "Tarso Marques": {
        "Race_Entries": 26.0,
        "Race_Starts": 24.0,
        "Pole_Positions": 0.0,
        "Race_Wins": 0.0,
        "Fastest_Laps": 0.0,
    },
    "Tom Bels\u00f8": {
        "Race_Entries": 5.0,
        "Race_Starts": 2.0,
        "Pole_Positions": 0.0,
        "Race_Wins": 0.0,
        "Fastest_Laps": 0.0,
    },
}


@staticmethod
def make_api_call(
    input_data: str = default_input_data,
    api_endpoint: str = "http://t-mobile-task.eu-west-1.elasticbeanstalk.com/graphql",
) -> None:
    """Make a GraphQL API call to the T-Mobile Task API."""
    query = """query PredictChampions($input: JSON!) {
        predictChampions(input: $input)
        }
        """
    variables = {"input": input_data}
    response = httpx.post(
        api_endpoint, json={"query": query, "variables": variables},
    )
    if response.status_code == STATUS_CODE_OK:
        data = response.json()
        if "errors" in data:
            print("GraphQL Error:", data["errors"])
        else:
            result = data["data"]["predictChampions"]
            print("Prediction Result:", result)
    else:
        print("HTTP Error:", response.status_code, response.text)
