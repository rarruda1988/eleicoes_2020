# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome6_from_dict(json.loads(json_string))

from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Estado:
    id: Optional[int]
    sigla: Optional[str]
    nome: str
    regiao: None
    cargos: None
    diretorios: None
    codigo: str
    capital: bool
    estado: Optional[str]

    def __init__(self, id: Optional[int], sigla: Optional[str], nome: str, regiao: None, cargos: None, diretorios: None, codigo: str, capital: bool, estado: Optional[str]) -> None:
        self.id = id
        self.sigla = sigla
        self.nome = nome
        self.regiao = regiao
        self.cargos = cargos
        self.diretorios = diretorios
        self.codigo = codigo
        self.capital = capital
        self.estado = estado

    @staticmethod
    def from_dict(obj: Any) -> 'Estado':
        assert isinstance(obj, dict)
        id = from_union([from_none, from_int], obj.get("id"))
        sigla = from_union([from_none, from_str], obj.get("sigla"))
        nome = from_str(obj.get("nome"))
        regiao = from_none(obj.get("regiao"))
        cargos = from_none(obj.get("cargos"))
        diretorios = from_none(obj.get("diretorios"))
        codigo = from_str(obj.get("codigo"))
        capital = from_bool(obj.get("capital"))
        estado = from_union([from_none, from_str], obj.get("estado"))
        return Estado(id, sigla, nome, regiao, cargos, diretorios, codigo, capital, estado)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_none, from_int], self.id)
        result["sigla"] = from_union([from_none, from_str], self.sigla)
        result["nome"] = from_str(self.nome)
        result["regiao"] = from_none(self.regiao)
        result["cargos"] = from_none(self.cargos)
        result["diretorios"] = from_none(self.diretorios)
        result["codigo"] = from_str(self.codigo)
        result["capital"] = from_bool(self.capital)
        result["estado"] = from_union([from_none, from_str], self.estado)
        return result


class EstadoMunicipio:
    estado: Estado
    municipios: List[Estado]

    def __init__(self, estado: Estado, municipios: List[Estado]) -> None:
        self.estado = estado
        self.municipios = municipios

    @staticmethod
    def from_dict(obj: Any) -> 'EstadoMunicipio':
        assert isinstance(obj, dict)
        estado = Estado.from_dict(obj.get("estado"))
        municipios = from_list(Estado.from_dict, obj.get("municipios"))
        return EstadoMunicipio(estado, municipios)

    def to_dict(self) -> dict:
        result: dict = {}
        result["estado"] = to_class(Estado, self.estado)
        result["municipios"] = from_list(lambda x: to_class(Estado, x), self.municipios)
        return result


def welcome6_from_dict(s: Any) -> EstadoMunicipio:
    return EstadoMunicipio.from_dict(s)


def welcome6_to_dict(x: EstadoMunicipio) -> Any:
    return to_class(EstadoMunicipio, x)
