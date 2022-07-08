from typing import Optional, Union

from src.color import FGColors, BGColors, SetBG8bit, SetFG8bit, SetFG24bit, SetBG24bit
from src.style import FontStyle

class formatText:
    __text: str
    options: Optional[Union[FGColors, BGColors, FontStyle, SetBG8bit, SetFG8bit, SetFG24bit, SetBG24bit]]
    
    def __init__(
        self,
        text: str,
        options: Optional[Union[FGColors, BGColors, FontStyle, SetBG8bit, SetFG8bit, SetFG24bit, SetBG24bit]] = None,
    ) -> None:
        self.__text = text
        self.options = options
    
    def __str__(self) -> str:
        if self.options is None:
            return self.__text
        
        else:
            code: str = "\033["
            for option in self.options:
                if isinstance(option, (FGColors, BGColors, FontStyle)):
                    code += f";{option.value}"
                    
                else:
                    code += f";{option}"
                
            return(f"{code}m{self.__text}\033[0m")