from strawberry import Schema


from .queries import PredictionQuery

from strawberry.extensions import QueryDepthLimiter, ValidationCache


schema = Schema(
    query=PredictionQuery,
    extensions=[QueryDepthLimiter(max_depth=10), ValidationCache(maxsize=100)],
)
