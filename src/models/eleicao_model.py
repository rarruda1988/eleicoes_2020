# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome7_from_dict(json.loads(json_string))

from enum import Enum
from typing import Optional, Any, List, TypeVar, Type, Callable, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class TipoAbrangencia(Enum):
    F = "F"
    M = "M"


class TipoEleicao(Enum):
    O = "O"


class Eleicao:
    id: int
    sigla_uf: None
    localidade_sg_ue: None
    ano: int
    codigo: None
    nome_eleicao: str
    tipo_eleicao: TipoEleicao
    turno: None
    tipo_abrangencia: TipoAbrangencia
    data_eleicao: Optional[datetime]
    cod_situacao_eleicao: None
    descricao_situacao_eleicao: None
    descricao_eleicao: int

    def __init__(self, id: int, sigla_uf: None, localidade_sg_ue: None, ano: int, codigo: None, nome_eleicao: str, tipo_eleicao: TipoEleicao, turno: None, tipo_abrangencia: TipoAbrangencia, data_eleicao: Optional[datetime], cod_situacao_eleicao: None, descricao_situacao_eleicao: None, descricao_eleicao: int) -> None:
        self.id = id
        self.sigla_uf = sigla_uf
        self.localidade_sg_ue = localidade_sg_ue
        self.ano = ano
        self.codigo = codigo
        self.nome_eleicao = nome_eleicao
        self.tipo_eleicao = tipo_eleicao
        self.turno = turno
        self.tipo_abrangencia = tipo_abrangencia
        self.data_eleicao = data_eleicao
        self.cod_situacao_eleicao = cod_situacao_eleicao
        self.descricao_situacao_eleicao = descricao_situacao_eleicao
        self.descricao_eleicao = descricao_eleicao

    @staticmethod
    def from_dict(obj: Any) -> 'Eleicao':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        sigla_uf = from_none(obj.get("siglaUF"))
        localidade_sg_ue = from_none(obj.get("localidadeSgUe"))
        ano = from_int(obj.get("ano"))
        codigo = from_none(obj.get("codigo"))
        nome_eleicao = from_str(obj.get("nomeEleicao"))
        tipo_eleicao = TipoEleicao(obj.get("tipoEleicao"))
        turno = from_none(obj.get("turno"))
        tipo_abrangencia = TipoAbrangencia(obj.get("tipoAbrangencia"))
        data_eleicao = from_union([from_none, from_datetime], obj.get("dataEleicao"))
        cod_situacao_eleicao = from_none(obj.get("codSituacaoEleicao"))
        descricao_situacao_eleicao = from_none(obj.get("descricaoSituacaoEleicao"))
        descricao_eleicao = int(from_str(obj.get("descricaoEleicao")))
        return Eleicao(id, sigla_uf, localidade_sg_ue, ano, codigo, nome_eleicao, tipo_eleicao, turno, tipo_abrangencia, data_eleicao, cod_situacao_eleicao, descricao_situacao_eleicao, descricao_eleicao)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["siglaUF"] = from_none(self.sigla_uf)
        result["localidadeSgUe"] = from_none(self.localidade_sg_ue)
        result["ano"] = from_int(self.ano)
        result["codigo"] = from_none(self.codigo)
        result["nomeEleicao"] = from_str(self.nome_eleicao)
        result["tipoEleicao"] = to_enum(TipoEleicao, self.tipo_eleicao)
        result["turno"] = from_none(self.turno)
        result["tipoAbrangencia"] = to_enum(TipoAbrangencia, self.tipo_abrangencia)
        result["dataEleicao"] = from_union([from_none, lambda x: x.isoformat()], self.data_eleicao)
        result["codSituacaoEleicao"] = from_none(self.cod_situacao_eleicao)
        result["descricaoSituacaoEleicao"] = from_none(self.descricao_situacao_eleicao)
        result["descricaoEleicao"] = from_str(str(self.descricao_eleicao))
        return result


def welcome7_from_dict(s: Any) -> List[Eleicao]:
    return from_list(Eleicao.from_dict, s)


def welcome7_to_dict(x: List[Eleicao]) -> Any:
    return from_list(lambda x: to_class(Eleicao, x), x)
