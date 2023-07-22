import strawberry
import typing

from strawberry.scalars import JSON
from strawberry.types import Info

from src.utils import model_predict_from_input


@strawberry.type
class PredictionQuery:
    @strawberry.field
    async def predict_champions(
        self,
        info: Info,
        input: JSON) -> JSON:
        try:
            ret_val: typing.Dict[str, float] = model_predict_from_input(info.context.model, input)
            return ret_val
        except Exception as e:
            raise Exception(str(e))
