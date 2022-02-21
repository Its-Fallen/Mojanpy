from typing import Dict, List, NamedTuple, Optional


class Name(NamedTuple):
    name: str
    changed_at: int
    created_at: Optional[int]

class Skin:
    def __init__(
        self,
        url: str,
        variant: str,
        id: Optional[str],
        state: Optional[str]
    ) -> None:
        self.__url = url
        self.__variant = variant
        self.__id = id
        self.__state = state

class Cape:
    def __init__(
        self,
        url: str,
        alias: Optional[str],
        id: Optional[str],
        state: Optional[str]
    ) -> None:
        pass