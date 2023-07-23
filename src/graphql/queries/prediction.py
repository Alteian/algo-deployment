import strawberry
import typing
import textwrap

from strawberry.scalars import JSON
from strawberry.types import Info

from src.utils import model_predict_from_input
from src.config.settings import BASE_DIR


@strawberry.type
class PredictionQuery:
    @strawberry.field(
    description="""Queries for the prediction of the F1 World Champions.
    Args --> variables:
    {
        "input": {
            "driver_name": {
                "Race_Entries": "float",
                "Race_Starts": "float",
                "Pole_Positions": "float",
                "Race_Wins": "float",
                "Fastest_Laps": "float"
            },
            ...
    }
        """,
        deprecation_reason="JSON input is generally not recommended as it cannot be typed. Better use GraphQL Objects with proper typing."
                 )
    async def predict_champions(
        self,
        info: Info,
        input: JSON) -> JSON:
        if not input:
            raise Exception("Input is empty.")
        try:
            ret_val: typing.Dict[str, float] = model_predict_from_input(info.context.model, input)
            return ret_val
        except Exception as e:
            raise Exception(str(e))

    @strawberry.field
    async def api_call_showcase(
        self,
        info: Info,
        ) -> str:
        with open(BASE_DIR / "graphql" / "programmatic" / "api_call.py", "r") as f:
            api_call_source = f.read()
            raw_string = textwrap.dedent(api_call_source)
        return raw_string
