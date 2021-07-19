import builtins
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

# The type of the values in a list, tuple or dict. Defaults to str unless `subcast` is used.
_SubType = TypeVar("_SubType")

class Env:
    # Preprocessor is omitted from the parameters because the type of argument passed to it, and its return type,
    # depends upon whether the default value is used (if the environment variable exists, the preprocessor is passed a
    # string; if it does not, it is passed whatever the value of `default` is). This behaviour makes it difficult to
    # know what type of argument will be passed to it and so it is recommended that it is not used.

    # A default value of `None` is not allowed by these type annotations for `list()`, `tuple()` or `dict()`.
    # This is to simplify the type annotations and encourage using a empty list/tuple/dict rather than None.

    # The `force` parameter is not allowed by these type annotations because it requires that `default` is a string,
    # rather than the type that will be returned by the method. Supporting this would complicate the type annotations.

    # schema parameter is not supported as it makes it impossible to infer the types returned by this class' methods.
    def __init__(self): ...
    # with default int
    @overload
    def int(
        self,
        var: str,
        default: int,
        *,
        postprocessor: Optional[Callable[[int], int]] = None,
    ) -> int: ...
    # with default `None`
    @overload
    def int(
        self,
        var: str,
        default: Optional[int],
        *,
        postprocessor: Optional[Callable[[Optional[int]], Optional[int]]] = None,
    ) -> Optional[int]: ...
    # without default
    @overload
    def int(
        self, var: str, *, postprocessor: Optional[Callable[[int], int]] = None,
    ) -> int: ...
    # with default float
    @overload
    def float(
        self,
        var: str,
        default: float,
        *,
        postprocessor: Optional[Callable[[float], float]] = None,
    ) -> float: ...
    # with default `None`
    @overload
    def float(
        self,
        var: str,
        default: Optional[float],
        *,
        postprocessor: Optional[Callable[[Optional[float]], Optional[float]]] = None,
    ) -> Optional[float]: ...
    # without default
    @overload
    def float(
        self, var: str, *, postprocessor: Optional[Callable[[float], float]] = None,
    ) -> float: ...
    # with subcast; with default list
    @overload
    def list(
        self,
        var: str,
        default: List[_SubType],
        *,
        subcast: Union[Type[_SubType], None, Callable[[str], _SubType]],
        postprocessor: Optional[Callable[[List[_SubType]], List[_SubType]]] = None,
    ) -> List[_SubType]: ...
    # without subcast; with default list
    @overload
    def list(
        self,
        var: str,
        default: List[str],
        *,
        postprocessor: Optional[Callable[[List[str]], List[str]]] = None,
    ) -> List[str]: ...
    # with subcast; without default
    @overload
    def list(
        self,
        var: str,
        *,
        subcast: Union[Type[_SubType], None, Callable[[str], _SubType]],
        postprocessor: Optional[Callable[[List[_SubType]], List[_SubType]]] = None,
    ) -> List[_SubType]: ...
    # without subcast; without default
    @overload
    def list(
        self,
        var: str,
        *,
        postprocessor: Optional[Callable[[List[str]], List[str]]] = None,
    ) -> List[str]: ...
    # with subcast; with default set
    @overload
    def set(
        self,
        var: str,
        default: Set[_SubType],
        *,
        subcast: Union[Type[_SubType], None, Callable[[str], _SubType]],
        postprocessor: Optional[Callable[[Set[_SubType]], Set[_SubType]]] = None,
    ) -> Set[_SubType]: ...
    # without subcast; with default set
    @overload
    def set(
        self,
        var: str,
        default: Set[str],
        *,
        postprocessor: Optional[Callable[[Set[str]], Set[str]]] = None,
    ) -> Set[str]: ...
    # with subcast; without default
    @overload
    def set(
        self,
        var: str,
        *,
        subcast: Union[Type[_SubType], None, Callable[[str], _SubType]],
        postprocessor: Optional[Callable[[Set[_SubType]], Set[_SubType]]] = None,
    ) -> Set[_SubType]: ...
    # without subcast; without default
    @overload
    def set(
        self,
        var: str,
        *,
        postprocessor: Optional[Callable[[Set[str]], Set[str]]] = None,
    ) -> Set[str]: ...
    # with subcast; with default tuple
    @overload
    def tuple(
        self,
        var: str,
        default: Tuple[_SubType, ...],
        *,
        subcast: Union[Type[_SubType], None, Callable[[str], _SubType]],
        postprocessor: Optional[
            Callable[[Tuple[_SubType, ...]], Tuple[_SubType, ...]]
        ] = None,
    ) -> Tuple[_SubType, ...]: ...
    # without subcast; with default tuple
    @overload
    def tuple(
        self,
        var: str,
        default: Tuple[str, ...],
        *,
        postprocessor: Optional[Callable[[Tuple[str, ...]], Tuple[str, ...]]] = None,
    ) -> Tuple[str, ...]: ...
    # with subcast; without default
    @overload
    def tuple(
        self,
        var: str,
        *,
        subcast: Union[Type[_SubType], None, Callable[[str], _SubType]],
        postprocessor: Optional[
            Callable[[Tuple[_SubType, ...]], Tuple[_SubType, ...]]
        ] = None,
    ) -> Tuple[_SubType, ...]: ...
    # without subcast; without default
    @overload
    def tuple(
        self,
        var: str,
        *,
        postprocessor: Optional[Callable[[Tuple[str, ...]], Tuple[str, ...]]] = None,
    ) -> Tuple[str, ...]: ...
    # with subcast; with default dict
    @overload
    def dict(
        self,
        var: str,
        default: Dict[str, _SubType],
        *,
        subcast: Union[Type[_SubType], None, Callable[[str], _SubType]],
        postprocessor: Optional[
            Callable[[Dict[str, _SubType]], Dict[str, _SubType]]
        ] = None,
    ) -> Dict[str, _SubType]: ...
    # without subcast; with default dict
    @overload
    def dict(
        self,
        var: str,
        default: Dict[str, str],
        *,
        postprocessor: Optional[Callable[[Dict[str, str]], Dict[str, str]]] = None,
    ) -> Dict[str, str]: ...
    # with subcast; without default
    @overload
    def dict(
        self,
        var: str,
        *,
        subcast: Union[Type[_SubType], None, Callable[[str], _SubType]],
        postprocessor: Optional[
            Callable[[Dict[str, _SubType]], Dict[str, _SubType]]
        ] = None,
    ) -> Dict[str, _SubType]: ...
    # without subcast; without default
    @overload
    def dict(
        self,
        var: str,
        *,
        postprocessor: Optional[Callable[[Dict[str, str]], Dict[str, str]]] = None,
    ) -> Dict[str, str]: ...
    # with default dict
    @overload
    def json(
        self,
        var: str,
        default: Dict[str, Any],
        *,
        postprocessor: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None,
    ) -> Dict[str, Any]: ...
    # with default `None`
    @overload
    def json(
        self,
        var: str,
        default: Optional[str],
        *,
        postprocessor: Optional[
            Callable[[Optional[Dict[str, Any]]], Optional[Dict[str, Any]]]
        ] = None,
    ) -> Optional[Dict[str, Any]]: ...
    # without default
    @overload
    def json(
        self,
        var: str,
        *,
        postprocessor: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None,
    ) -> Dict[str, Any]: ...
    # with default str
    @overload
    def str(
        self,
        var: str,
        default: str,
        *,
        postprocessor: Optional[Callable[[str], str]] = None,
    ) -> str: ...
    # with default `None`
    @overload
    def str(
        self,
        var: str,
        default: Optional[str],
        *,
        postprocessor: Optional[Callable[[Optional[str]], Optional[str]]] = None,
    ) -> Optional[str]: ...
    # without default
    @overload
    def str(
        self, var: str, *, postprocessor: Optional[Callable[[str], str]] = None,
    ) -> str: ...
    # with default bool
    @overload
    def bool(
        self,
        var: builtins.str,
        default: bool,
        *,
        postprocessor: Optional[Callable[[bool], bool]] = None,
    ) -> bool: ...
    # with default `None`
    @overload
    def bool(
        self,
        var: builtins.str,
        default: Optional[bool],
        *,
        postprocessor: Optional[Callable[[Optional[bool]], Optional[bool]]] = None,
    ) -> Optional[bool]: ...
    # without default
    @overload
    def bool(
        self,
        var: builtins.str,
        *,
        postprocessor: Optional[Callable[[bool], bool]] = None,
    ) -> bool: ...
    @staticmethod
    def read_envfile(
        path: Optional[builtins.str] = None, **overrides: builtins.str
    ): ...

env: Env
