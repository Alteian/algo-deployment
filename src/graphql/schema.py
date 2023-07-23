from strawberry import Schema
from strawberry.extensions import QueryDepthLimiter, ValidationCache

from .queries import PredictionQuery

schema = Schema(
    query=PredictionQuery,
    extensions=[QueryDepthLimiter(max_depth=10), ValidationCache(maxsize=100)],
)
