from typing import Optional, Union

from src.format import *

def decoterm(
    *args,
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
    ] = [],
    **kwargs,
) -> None:
    orders:list = []
    
    for arg in args:
        for option in options:
            if isinstance(option, (FG_Colors, BG_Colors, Font_Style)):
                orders.append(option)

    print(FormatText(arg, options=orders), **kwargs)