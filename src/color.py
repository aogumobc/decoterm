from enum import Enum

class FG_Colors(Enum):
    BLACK          = 30
    RED            = 31
    GREEN          = 32
    YELLOW         = 33
    BLUE           = 34
    MAGENTA        = 35
    CYAN           = 36
    WHITE          = 37
    DEFAULT        = 39
    BRIGHT_BLACK   = 90
    BRIGHT_RED     = 91
    BRIGHT_GREEN   = 92
    BRIGHT_YELLOW  = 93
    BRIGHT_BLUE    = 94
    BRIGHT_MAGENTA = 95
    BRIGHT_CYAN    = 96
    BRIGHT_WHITE   = 97

class BG_Colors(Enum):
    BLACK          = 40
    RED            = 41
    GREEN          = 42
    YELLOW         = 43
    BLUE           = 44
    MAGENTA        = 45
    CYAN           = 46
    WHITE          = 47
    DEFAULT        = 49
    BRIGHT_BLACK   = 100
    BRIGHT_RED     = 101
    BRIGHT_GREEN   = 102
    BRIGHT_YELLOW  = 103
    BRIGHT_BLUE    = 104
    BRIGHT_MAGENTA = 105
    BRIGHT_CYAN    = 106
    BRIGHT_WHITE   = 107

class SetFG_8bit:
    __n:int

    def __init__(
        self,
        n:int
    ) -> None:
        if not ( 0 <= n <= 255 ):
            raise Exception(f"The number MUST be in the range 0-255 but you entered {n}")

        self.__n = n

    def __str__(self) -> str:
        return f"\033[38;5;{self.__n}m"

class SetBG_8bit:
    __n:int

    def __init__(
        self,
        n:int
    ) -> None:
        if not ( 0 <= n <= 255 ):
            raise Exception(f"The number MUST be in the range 0-255 but you entered {n}")

        self.__n = n

    def __str__(self) -> str:
        return f"\033[48;5;{self.__n}m"

class SetFG_24bit:
    __r:int
    __g:int
    __b:int

    def __init__(
        self,
        r:int,
        g:int,
        b:int,
    ) -> None:
        for c, n in { 'R':r, 'G':g, 'B':b }.items():
            if not ( 0 <= n <= 255 ):
                raise Exception(f"The number MUST be in the range 0-255 but you entered '{n} on {c}'")

            self.__r = r
            self.__g = g
            self.__b = b

    def __str__(self) -> str:
        return f"\033[38;2;{self.__r};{self.__g};{self.__b}m"

class SetBG_24bit:
    __r:int
    __g:int
    __b:int

    def __init__(
        self,
        r:int,
        g:int,
        b:int,
    ) -> None:
        for c, n in { 'R':r, 'G':g, 'B':b }.items():
            if not ( 0 <= n <= 255 ):
                raise Exception(f"The number MUST be in the range 0-255 but you entered '{n} on {c}'")

            self.__r = r
            self.__g = g
            self.__b = b

    def __str__(self) -> str:
        return f"\033[48;2;{self.__r};{self.__g};{self.__b}m"