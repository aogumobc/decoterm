from typing import Optional, Union

from color import *
from style import *

class FormatText:
    __text:str
    __options:Optional[
        Union[
            FG_Colors,
            BG_Colors,
            Font_Style,
            SetFG_8bit,
            SetBG_8bit,
            SetFG_24bit,
            SetBG_24bit
        ]
    ]

    def __init__(
        self,
        text:str,
        options:Optional[
            Union[
                FG_Colors,
                BG_Colors,
                Font_Style,
                SetFG_8bit,
                SetBG_8bit,
                SetFG_24bit,
                SetBG_24bit
            ]
        ]
    ) -> None:
        self.__text = text
        self.__options = options

    def __str__(self) -> str:
        if self.__options is None:
            return self.__text

        else:
            code:str = "\033["
            
            for option in self.__options:
                if isinstance(option, (FG_Colors, BG_Colors, Font_Style)):
                    code += f";{option.value}"

                else:
                    code += f";{option}"

            return f"{code}m{self.__text}\033[0m"