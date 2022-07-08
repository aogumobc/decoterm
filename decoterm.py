from typing import Optional, Union

from src.format import *

def decoterm(
    *args,
    options: Optional[Union[FGColors, BGColors, FontStyle, SetBG8bit, SetFG8bit, SetFG24bit, SetBG24bit]] = [],
    **kwargs,
) -> None:
    
    order: list = []
    for arg in args:
        for option in options:
            if isinstance(option, (FGColors, BGColors, FontStyle)):
                order.append(option)
            
    print(formatText(arg, options=order), **kwargs)