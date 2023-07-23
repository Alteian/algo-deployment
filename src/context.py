from typing import Union
from starlette.requests import Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from functools import cached_property


class CustomContext:
    def __init__(
        self,
        request: Union[Request, WebSocket],
        response: Response,
    ) -> None:
        self.request = request
        self.response = response

    request: Union[Request, WebSocket]
    response: Response

    @cached_property
    def model(self):
        return "src/algo/model.pickle"
