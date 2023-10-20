import app.command_types as cmdtype
from typing import List, Union


class Command:
    def __init__(
        self,
        command_name: Union[cmdtype.InputCommandType, cmdtype.OutputCommandType],
        params: List[str],
    ) -> None:
        self.command_name = command_name
        self.params = params
