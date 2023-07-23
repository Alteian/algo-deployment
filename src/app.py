from typing import Union
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from strawberry.asgi import GraphQL

from src.graphql import schema
from src.context import CustomContext


class CustomGraphQL(GraphQL):
    async def get_context(
        self, 
        request: Union[Request, WebSocket],
        response: Response,
    ) -> CustomContext:
        return CustomContext(request=request, response=response)


graphql_app = CustomGraphQL(schema)

app = Starlette()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
