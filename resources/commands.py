from dataclasses import dataclass
from typing import Union

import marshmallow_dataclass


@dataclass
class Commands:
    file_name: str
    cmd1: str
    value1: Union[str, int]
    cmd2: str
    value2: Union[str, int]


CommandsSchema = marshmallow_dataclass.class_schema(Commands)
