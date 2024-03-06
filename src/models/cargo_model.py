# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome2_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


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


class CargoDetail:
    codigo: int
    sigla: None
    nome: str
    cod_superior: int
    titular: bool
    contagem: int

    def __init__(self, codigo: int, sigla: None, nome: str, cod_superior: int, titular: bool, contagem: int) -> None:
        self.codigo = codigo
        self.sigla = sigla
        self.nome = nome
        self.cod_superior = cod_superior
        self.titular = titular
        self.contagem = contagem

    @staticmethod
    def from_dict(obj: Any) -> 'CargoDetail':
        assert isinstance(obj, dict)
        codigo = from_int(obj.get("codigo"))
        sigla = from_none(obj.get("sigla"))
        nome = from_str(obj.get("nome"))
        cod_superior = from_int(obj.get("codSuperior"))
        titular = from_bool(obj.get("titular"))
        contagem = from_int(obj.get("contagem"))
        return CargoDetail(codigo, sigla, nome, cod_superior, titular, contagem)

    def to_dict(self) -> dict:
        result: dict = {}
        result["codigo"] = from_int(self.codigo)
        result["sigla"] = from_none(self.sigla)
        result["nome"] = from_str(self.nome)
        result["codSuperior"] = from_int(self.cod_superior)
        result["titular"] = from_bool(self.titular)
        result["contagem"] = from_int(self.contagem)
        return result


class UnidadeEleitoralDTO:
    id: None
    sigla: str
    nome: str
    regiao: None
    cargos: None
    diretorios: None
    codigo: int
    capital: bool
    estado: str

    def __init__(self, id: None, sigla: str, nome: str, regiao: None, cargos: None, diretorios: None, codigo: int, capital: bool, estado: str) -> None:
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
    def from_dict(obj: Any) -> 'UnidadeEleitoralDTO':
        assert isinstance(obj, dict)
        id = from_none(obj.get("id"))
        sigla = from_str(obj.get("sigla"))
        nome = from_str(obj.get("nome"))
        regiao = from_none(obj.get("regiao"))
        cargos = from_none(obj.get("cargos"))
        diretorios = from_none(obj.get("diretorios"))
        codigo = int(from_str(obj.get("codigo")))
        capital = from_bool(obj.get("capital"))
        estado = from_str(obj.get("estado"))
        return UnidadeEleitoralDTO(id, sigla, nome, regiao, cargos, diretorios, codigo, capital, estado)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_none(self.id)
        result["sigla"] = from_str(self.sigla)
        result["nome"] = from_str(self.nome)
        result["regiao"] = from_none(self.regiao)
        result["cargos"] = from_none(self.cargos)
        result["diretorios"] = from_none(self.diretorios)
        result["codigo"] = from_str(str(self.codigo))
        result["capital"] = from_bool(self.capital)
        result["estado"] = from_str(self.estado)
        return result


class Cargo:
    unidade_eleitoral_dto: UnidadeEleitoralDTO
    cargos: List[CargoDetail]

    def __init__(self, unidade_eleitoral_dto: UnidadeEleitoralDTO, cargos: List[CargoDetail]) -> None:
        self.unidade_eleitoral_dto = unidade_eleitoral_dto
        self.cargos = cargos

    @staticmethod
    def from_dict(obj: Any) -> 'Cargo':
        assert isinstance(obj, dict)
        unidade_eleitoral_dto = UnidadeEleitoralDTO.from_dict(obj.get("unidadeEleitoralDTO"))
        cargos = from_list(CargoDetail.from_dict, obj.get("cargos"))
        return Cargo(unidade_eleitoral_dto, cargos)

    def to_dict(self) -> dict:
        result: dict = {}
        result["unidadeEleitoralDTO"] = to_class(UnidadeEleitoralDTO, self.unidade_eleitoral_dto)
        result["cargos"] = from_list(lambda x: to_class(CargoDetail, x), self.cargos)
        return result


def welcome2_from_dict(s: Any) -> Cargo:
    return Cargo.from_dict(s)


def welcome2_to_dict(x: Cargo) -> Any:
    return to_class(Cargo, x)
