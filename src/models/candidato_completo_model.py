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
#     result = welcome9_from_dict(json.loads(json_string))
import dateutil.parser

from typing import Any, List, TypeVar, Callable, Type, cast
from datetime import datetime

from models.cargo_model import CargoDetail


T = TypeVar("T")


def from_int(x: Any) -> int:
    if not x:
        return 0
    else:
        int(x)
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    if not x:
        return ""
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_float(x: Any) -> float:
    if not x:
        return 0.0
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_datetime(x: Any) -> datetime:
    if not x:
        return datetime(1900,1,1)
    return dateutil.parser.parse(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_bool(x: Any) -> bool:
    if not x:
        return False
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    if not x:
        return []

    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Substituto:
    sq_eleicao: int
    sq_candidato: int
    sg_ue: int
    nr_ano: int
    nm_candidato: str
    url: str

    def __init__(self, sq_eleicao: int, sq_candidato: int, sg_ue: int, nr_ano: int, nm_candidato: str, url: str) -> None:
        self.sq_eleicao = sq_eleicao
        self.sq_candidato = sq_candidato
        self.sg_ue = sg_ue
        self.nr_ano = nr_ano
        self.nm_candidato = nm_candidato
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'Substituto':
        if not obj:
            return None
        assert isinstance(obj, dict)
        sq_eleicao = from_int(obj.get("sqEleicao"))
        sq_candidato = from_int(obj.get("sqCandidato"))
        sg_ue = int(from_str(obj.get("sgUe")))
        nr_ano = from_int(obj.get("nrAno"))
        nm_candidato = from_str(obj.get("nmCandidato"))
        url = from_str(obj.get("url"))
        return Substituto(sq_eleicao, sq_candidato, sg_ue, nr_ano, nm_candidato, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sqEleicao"] = from_int(self.sq_eleicao)
        result["sqCandidato"] = from_int(self.sq_candidato)
        result["sgUe"] = from_str(str(self.sg_ue))
        result["nrAno"] = from_int(self.nr_ano)
        result["nmCandidato"] = from_str(self.nm_candidato)
        result["url"] = from_str(self.url)
        return result


class Arquivo:
    id_arquivo: int
    nome: str
    url: str
    tipo: str
    cod_tipo: int
    full_file_path: None
    file_input_stream: None
    file_byte_array: None

    def __init__(self, id_arquivo: int, nome: str, url: str, tipo: str, cod_tipo: int, full_file_path: None, file_input_stream: None, file_byte_array: None) -> None:
        self.id_arquivo = id_arquivo
        self.nome = nome
        self.url = url
        self.tipo = tipo
        self.cod_tipo = cod_tipo
        self.full_file_path = full_file_path
        self.file_input_stream = file_input_stream
        self.file_byte_array = file_byte_array

    @staticmethod
    def from_dict(obj: Any) -> 'Arquivo':
        assert isinstance(obj, dict)
        id_arquivo = from_int(obj.get("idArquivo"))
        nome = from_str(obj.get("nome"))
        url = from_str(obj.get("url"))
        tipo = from_str(obj.get("tipo"))
        cod_tipo = int(from_str(obj.get("codTipo")))
        full_file_path = from_none(obj.get("fullFilePath"))
        file_input_stream = from_none(obj.get("fileInputStream"))
        file_byte_array = from_none(obj.get("fileByteArray"))
        return Arquivo(id_arquivo, nome, url, tipo, cod_tipo, full_file_path, file_input_stream, file_byte_array)

    def to_dict(self) -> dict:
        result: dict = {}
        result["idArquivo"] = from_int(self.id_arquivo)
        result["nome"] = from_str(self.nome)
        result["url"] = from_str(self.url)
        result["tipo"] = from_str(self.tipo)
        result["codTipo"] = from_str(str(self.cod_tipo))
        result["fullFilePath"] = from_none(self.full_file_path)
        result["fileInputStream"] = from_none(self.file_input_stream)
        result["fileByteArray"] = from_none(self.file_byte_array)
        return result


class Ben:
    ordem: int
    descricao: str
    descricao_de_tipo_de_bem: str
    valor: float
    data_ultima_atualizacao: datetime

    def __init__(self, ordem: int, descricao: str, descricao_de_tipo_de_bem: str, valor: float, data_ultima_atualizacao: datetime) -> None:
        self.ordem = ordem
        self.descricao = descricao
        self.descricao_de_tipo_de_bem = descricao_de_tipo_de_bem
        self.valor = valor
        self.data_ultima_atualizacao = data_ultima_atualizacao

    @staticmethod
    def from_dict(obj: Any) -> 'Ben':
        assert isinstance(obj, dict)
        ordem = from_int(obj.get("ordem"))
        descricao = from_str(obj.get("descricao"))
        descricao_de_tipo_de_bem = from_str(obj.get("descricaoDeTipoDeBem"))
        valor = from_float(obj.get("valor"))
        data_ultima_atualizacao = from_datetime(
            obj.get("dataUltimaAtualizacao"))
        return Ben(ordem, descricao, descricao_de_tipo_de_bem, valor, data_ultima_atualizacao)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ordem"] = from_int(self.ordem)
        result["descricao"] = from_str(self.descricao)
        result["descricaoDeTipoDeBem"] = from_str(
            self.descricao_de_tipo_de_bem)
        result["valor"] = to_float(self.valor)
        result["dataUltimaAtualizacao"] = self.data_ultima_atualizacao.isoformat()
        return result


class Eleicao:
    id: int
    sigla_uf: None
    localidade_sg_ue: None
    ano: int
    codigo: None
    nome_eleicao: None
    tipo_eleicao: None
    turno: None
    tipo_abrangencia: None
    data_eleicao: None
    cod_situacao_eleicao: None
    descricao_situacao_eleicao: None
    descricao_eleicao: int

    def __init__(self, id: int, sigla_uf: None, localidade_sg_ue: None, ano: int, codigo: None, nome_eleicao: None, tipo_eleicao: None, turno: None, tipo_abrangencia: None, data_eleicao: None, cod_situacao_eleicao: None, descricao_situacao_eleicao: None, descricao_eleicao: int) -> None:
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
        nome_eleicao = from_none(obj.get("nomeEleicao"))
        tipo_eleicao = from_none(obj.get("tipoEleicao"))
        turno = from_none(obj.get("turno"))
        tipo_abrangencia = from_none(obj.get("tipoAbrangencia"))
        data_eleicao = from_none(obj.get("dataEleicao"))
        cod_situacao_eleicao = from_none(obj.get("codSituacaoEleicao"))
        descricao_situacao_eleicao = from_none(
            obj.get("descricaoSituacaoEleicao"))
        descricao_eleicao = int(from_str(obj.get("descricaoEleicao")))
        return Eleicao(id, sigla_uf, localidade_sg_ue, ano, codigo, nome_eleicao, tipo_eleicao, turno, tipo_abrangencia, data_eleicao, cod_situacao_eleicao, descricao_situacao_eleicao, descricao_eleicao)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["siglaUF"] = from_none(self.sigla_uf)
        result["localidadeSgUe"] = from_none(self.localidade_sg_ue)
        result["ano"] = from_int(self.ano)
        result["codigo"] = from_none(self.codigo)
        result["nomeEleicao"] = from_none(self.nome_eleicao)
        result["tipoEleicao"] = from_none(self.tipo_eleicao)
        result["turno"] = from_none(self.turno)
        result["tipoAbrangencia"] = from_none(self.tipo_abrangencia)
        result["dataEleicao"] = from_none(self.data_eleicao)
        result["codSituacaoEleicao"] = from_none(self.cod_situacao_eleicao)
        result["descricaoSituacaoEleicao"] = from_none(
            self.descricao_situacao_eleicao)
        result["descricaoEleicao"] = from_str(str(self.descricao_eleicao))
        return result


class EleicoesAnteriore:
    nr_ano: int
    id: str
    nome_urna: str
    nome_candidato: str
    id_eleicao: int
    sg_ue: str
    local: str
    cargo: str
    partido: str
    situacao_totalizacao: str
    tx_link: str

    def __init__(self, nr_ano: int, id: str, nome_urna: str, nome_candidato: str, id_eleicao: int, sg_ue: str, local: str, cargo: str, partido: str, situacao_totalizacao: str, tx_link: str) -> None:
        self.nr_ano = nr_ano
        self.id = id
        self.nome_urna = nome_urna
        self.nome_candidato = nome_candidato
        self.id_eleicao = id_eleicao
        self.sg_ue = sg_ue
        self.local = local
        self.cargo = cargo
        self.partido = partido
        self.situacao_totalizacao = situacao_totalizacao
        self.tx_link = tx_link

    @staticmethod
    def from_dict(obj: Any) -> 'EleicoesAnteriore':
        assert isinstance(obj, dict)
        nr_ano = from_int(obj.get("nrAno"))
        id = from_str(obj.get("id"))
        nome_urna = from_str(obj.get("nomeUrna"))
        nome_candidato = from_str(obj.get("nomeCandidato"))
        id_eleicao = int(from_str(obj.get("idEleicao")))
        sg_ue = from_str(obj.get("sgUe"))
        local = from_str(obj.get("local"))
        cargo = from_str(obj.get("cargo"))
        partido = from_str(obj.get("partido"))
        situacao_totalizacao = from_str(obj.get("situacaoTotalizacao"))
        tx_link = from_str(obj.get("txLink"))
        return EleicoesAnteriore(nr_ano, id, nome_urna, nome_candidato, id_eleicao, sg_ue, local, cargo, partido, situacao_totalizacao, tx_link)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nrAno"] = from_int(self.nr_ano)
        result["id"] = from_str(self.id)
        result["nomeUrna"] = from_str(self.nome_urna)
        result["nomeCandidato"] = from_str(self.nome_candidato)
        result["idEleicao"] = from_str(str(self.id_eleicao))
        result["sgUe"] = from_str(self.sg_ue)
        result["local"] = from_str(self.local)
        result["cargo"] = from_str(self.cargo)
        result["partido"] = from_str(self.partido)
        result["situacaoTotalizacao"] = from_str(self.situacao_totalizacao)
        result["txLink"] = from_str(self.tx_link)
        return result


class Partido:
    numero: int
    sigla: str
    nome: str

    def __init__(self, numero: int, sigla: str, nome: str) -> None:
        self.numero = numero
        self.sigla = sigla
        self.nome = nome

    @staticmethod
    def from_dict(obj: Any) -> 'Partido':
        assert isinstance(obj, dict)
        numero = from_int(obj.get("numero"))
        sigla = from_str(obj.get("sigla"))
        nome = from_str(obj.get("nome"))
        return Partido(numero, sigla, nome)

    def to_dict(self) -> dict:
        result: dict = {}
        result["numero"] = from_int(self.numero)
        result["sigla"] = from_str(self.sigla)
        result["nome"] = from_str(self.nome)
        return result


class Vice:
    dt_ultima_atualizacao: datetime
    nome_coligacao: None
    composicao_coligacao: None
    st_registro: None
    situacao_candidato: None
    url_foto: str
    sg_ue: int
    sq_eleicao: int
    vice_dt_ultima_atualizacao: int
    sq_candidato_superior: int
    nr_candidato: int
    nm_urna: str
    nm_candidato: str
    ds_cargo: str
    nm_partido: str
    sg_partido: str
    sq_candidato: int

    def __init__(self, dt_ultima_atualizacao: datetime, nome_coligacao: None, composicao_coligacao: None, st_registro: None, situacao_candidato: None, url_foto: str, sg_ue: int, sq_eleicao: int, vice_dt_ultima_atualizacao: int, sq_candidato_superior: int, nr_candidato: int, nm_urna: str, nm_candidato: str, ds_cargo: str, nm_partido: str, sg_partido: str, sq_candidato: int) -> None:
        self.dt_ultima_atualizacao = dt_ultima_atualizacao
        self.nome_coligacao = nome_coligacao
        self.composicao_coligacao = composicao_coligacao
        self.st_registro = st_registro
        self.situacao_candidato = situacao_candidato
        self.url_foto = url_foto
        self.sg_ue = sg_ue
        self.sq_eleicao = sq_eleicao
        self.vice_dt_ultima_atualizacao = vice_dt_ultima_atualizacao
        self.sq_candidato_superior = sq_candidato_superior
        self.nr_candidato = nr_candidato
        self.nm_urna = nm_urna
        self.nm_candidato = nm_candidato
        self.ds_cargo = ds_cargo
        self.nm_partido = nm_partido
        self.sg_partido = sg_partido
        self.sq_candidato = sq_candidato

    @staticmethod
    def from_dict(obj: Any) -> 'Vice':
        assert isinstance(obj, dict)
        dt_ultima_atualizacao = from_datetime(obj.get("DT_ULTIMA_ATUALIZACAO"))
        nome_coligacao = from_str(obj.get("nomeColigacao"))
        composicao_coligacao = from_str(obj.get("composicaoColigacao"))
        st_registro = from_bool(obj.get("stRegistro"))
        situacao_candidato = from_str(obj.get("situacaoCandidato"))
        url_foto = from_str(obj.get("urlFoto"))
        sg_ue = int(from_str(obj.get("sg_UE")))
        sq_eleicao = from_int(obj.get("sq_ELEICAO"))
        vice_dt_ultima_atualizacao = from_int(obj.get("dt_ULTIMA_ATUALIZACAO"))
        sq_candidato_superior = from_int(obj.get("sq_CANDIDATO_SUPERIOR"))
        nr_candidato = int(from_str(obj.get("nr_CANDIDATO")))
        nm_urna = from_str(obj.get("nm_URNA"))
        nm_candidato = from_str(obj.get("nm_CANDIDATO"))
        ds_cargo = from_str(obj.get("ds_CARGO"))
        nm_partido = from_str(obj.get("nm_PARTIDO"))
        sg_partido = from_str(obj.get("sg_PARTIDO"))
        sq_candidato = from_int(obj.get("sq_CANDIDATO"))
        return Vice(dt_ultima_atualizacao, nome_coligacao, composicao_coligacao, st_registro, situacao_candidato, url_foto, sg_ue, sq_eleicao, vice_dt_ultima_atualizacao, sq_candidato_superior, nr_candidato, nm_urna, nm_candidato, ds_cargo, nm_partido, sg_partido, sq_candidato)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DT_ULTIMA_ATUALIZACAO"] = self.dt_ultima_atualizacao.isoformat()
        result["nomeColigacao"] = from_none(self.nome_coligacao)
        result["composicaoColigacao"] = from_none(self.composicao_coligacao)
        result["stRegistro"] = from_none(self.st_registro)
        result["situacaoCandidato"] = from_none(self.situacao_candidato)
        result["urlFoto"] = from_str(self.url_foto)
        result["sg_UE"] = from_str(str(self.sg_ue))
        result["sq_ELEICAO"] = from_int(self.sq_eleicao)
        result["dt_ULTIMA_ATUALIZACAO"] = from_int(
            self.vice_dt_ultima_atualizacao)
        result["sq_CANDIDATO_SUPERIOR"] = from_int(self.sq_candidato_superior)
        result["nr_CANDIDATO"] = from_str(str(self.nr_candidato))
        result["nm_URNA"] = from_str(self.nm_urna)
        result["nm_CANDIDATO"] = from_str(self.nm_candidato)
        result["ds_CARGO"] = from_str(self.ds_cargo)
        result["nm_PARTIDO"] = from_str(self.nm_partido)
        result["sg_PARTIDO"] = from_str(self.sg_partido)
        result["sq_CANDIDATO"] = from_int(self.sq_candidato)
        return result


class CandidatoCompleto:
    id: int
    nome_urna: str
    numero: int
    id_candidato_superior: int
    nome_completo: str
    descricao_sexo: str
    data_de_nascimento: datetime
    titulo_eleitor: str
    cpf: str
    descricao_estado_civil: str
    descricao_cor_raca: str
    descricao_situacao: str
    nacionalidade: str
    grau_instrucao: str
    ocupacao: str
    gasto_campanha1_t: float
    gasto_campanha2_t: int
    sg_uf_nascimento: str
    nome_municipio_nascimento: str
    local_candidatura: str
    uf_candidatura: int
    uf_superior_candidatura: str
    data_ultima_atualizacao: datetime
    foto_url: str
    foto_data_ultima_atualizacao: datetime
    descricao_totalizacao: str
    nome_coligacao: str
    composicao_coligacao: str
    descricao_tipo_drap: str
    numero_processo_drap: str
    numero_processo_drap_encrypt: str
    numero_processo: str
    numero_processo_encrypt: str
    numero_processo_prest_contas: None
    numero_processo_prest_contas_encrypt: None
    numero_protocolo: int
    cargo: CargoDetail
    bens: List[Ben]
    total_de_bens: int
    vices: List[Vice]
    partido: Partido
    eleicao: Eleicao
    emails: List[str]
    sites: List[Any]
    arquivos: List[Arquivo]
    eleicoes_anteriores: List[EleicoesAnteriore]
    substituto: Substituto
    motivos: None
    codigo_situacao_candidato: int
    descricao_situacao_candidato: None
    is_candidato_inapto: bool
    codigo_situacao_partido: str
    descricao_situacao_partido: str
    is_cand_fechado: bool
    cnpjcampanha: str
    gasto_campanha: float
    st_substituido: bool
    st_motivo_ficha_limpa: bool
    st_motivo_abuso_poder: bool
    st_motivo_compra_voto: bool
    st_motivo_conduta_vedada: bool
    st_motivo_gasto_ilicito: bool
    ds_motivo_outros: None
    st_motivo_ausencia_requisito: bool
    st_motivo_ind_partido: bool
    st_divulga: bool
    st_divulga_bens: bool
    st_reeleicao: bool
    st_divulga_arquivos: bool
    descricao_naturalidade: str
    url: str

    def __init__(self, id: int, nome_urna: str, numero: int, id_candidato_superior: int, nome_completo: str, descricao_sexo: str, data_de_nascimento: datetime, titulo_eleitor: str, cpf: str, descricao_estado_civil: str, descricao_cor_raca: str, descricao_situacao: str, nacionalidade: str, grau_instrucao: str, ocupacao: str, gasto_campanha1_t: float, gasto_campanha2_t: int, sg_uf_nascimento: str, nome_municipio_nascimento: str, local_candidatura: str, uf_candidatura: int, uf_superior_candidatura: str, data_ultima_atualizacao: datetime, foto_url: str, foto_data_ultima_atualizacao: datetime, descricao_totalizacao: str, nome_coligacao: str, composicao_coligacao: str, descricao_tipo_drap: str, numero_processo_drap: str, numero_processo_drap_encrypt: str, numero_processo: str, numero_processo_encrypt: str, numero_processo_prest_contas: None, numero_processo_prest_contas_encrypt: None, numero_protocolo: int, cargo: CargoDetail, bens: List[Ben], total_de_bens: int, vices: List[Vice], partido: Partido, eleicao: Eleicao, emails: List[str], sites: List[Any], arquivos: List[Arquivo], eleicoes_anteriores: List[EleicoesAnteriore], substituto: Substituto, motivos: None, codigo_situacao_candidato: int, descricao_situacao_candidato: None, is_candidato_inapto: bool, codigo_situacao_partido: str, descricao_situacao_partido: str, is_cand_fechado: bool, cnpjcampanha: str, gasto_campanha: float, st_substituido: bool, st_motivo_ficha_limpa: bool, st_motivo_abuso_poder: bool, st_motivo_compra_voto: bool, st_motivo_conduta_vedada: bool, st_motivo_gasto_ilicito: bool, ds_motivo_outros: None, st_motivo_ausencia_requisito: bool, st_motivo_ind_partido: bool, st_divulga: bool, st_divulga_bens: bool, st_reeleicao: bool, st_divulga_arquivos: bool, descricao_naturalidade: str, url: str) -> None:
        self.id = id
        self.nome_urna = nome_urna
        self.numero = numero
        self.id_candidato_superior = id_candidato_superior
        self.nome_completo = nome_completo
        self.descricao_sexo = descricao_sexo
        self.data_de_nascimento = data_de_nascimento
        self.titulo_eleitor = titulo_eleitor
        self.cpf = cpf
        self.descricao_estado_civil = descricao_estado_civil
        self.descricao_cor_raca = descricao_cor_raca
        self.descricao_situacao = descricao_situacao
        self.nacionalidade = nacionalidade
        self.grau_instrucao = grau_instrucao
        self.ocupacao = ocupacao
        self.gasto_campanha1_t = gasto_campanha1_t
        self.gasto_campanha2_t = gasto_campanha2_t
        self.sg_uf_nascimento = sg_uf_nascimento
        self.nome_municipio_nascimento = nome_municipio_nascimento
        self.local_candidatura = local_candidatura
        self.uf_candidatura = uf_candidatura
        self.uf_superior_candidatura = uf_superior_candidatura
        self.data_ultima_atualizacao = data_ultima_atualizacao
        self.foto_url = foto_url
        self.foto_data_ultima_atualizacao = foto_data_ultima_atualizacao
        self.descricao_totalizacao = descricao_totalizacao
        self.nome_coligacao = nome_coligacao
        self.composicao_coligacao = composicao_coligacao
        self.descricao_tipo_drap = descricao_tipo_drap
        self.numero_processo_drap = numero_processo_drap
        self.numero_processo_drap_encrypt = numero_processo_drap_encrypt
        self.numero_processo = numero_processo
        self.numero_processo_encrypt = numero_processo_encrypt
        self.numero_processo_prest_contas = numero_processo_prest_contas
        self.numero_processo_prest_contas_encrypt = numero_processo_prest_contas_encrypt
        self.numero_protocolo = numero_protocolo
        self.cargo = cargo
        self.bens = bens
        self.total_de_bens = total_de_bens
        self.vices = vices
        self.partido = partido
        self.eleicao = eleicao
        self.emails = emails
        self.sites = sites
        self.arquivos = arquivos
        self.eleicoes_anteriores = eleicoes_anteriores
        self.substituto = substituto
        self.motivos = motivos
        self.codigo_situacao_candidato = codigo_situacao_candidato
        self.descricao_situacao_candidato = descricao_situacao_candidato
        self.is_candidato_inapto = is_candidato_inapto
        self.codigo_situacao_partido = codigo_situacao_partido
        self.descricao_situacao_partido = descricao_situacao_partido
        self.is_cand_fechado = is_cand_fechado
        self.cnpjcampanha = cnpjcampanha
        self.gasto_campanha = gasto_campanha
        self.st_substituido = st_substituido
        self.st_motivo_ficha_limpa = st_motivo_ficha_limpa
        self.st_motivo_abuso_poder = st_motivo_abuso_poder
        self.st_motivo_compra_voto = st_motivo_compra_voto
        self.st_motivo_conduta_vedada = st_motivo_conduta_vedada
        self.st_motivo_gasto_ilicito = st_motivo_gasto_ilicito
        self.ds_motivo_outros = ds_motivo_outros
        self.st_motivo_ausencia_requisito = st_motivo_ausencia_requisito
        self.st_motivo_ind_partido = st_motivo_ind_partido
        self.st_divulga = st_divulga
        self.st_divulga_bens = st_divulga_bens
        self.st_reeleicao = st_reeleicao
        self.st_divulga_arquivos = st_divulga_arquivos
        self.descricao_naturalidade = descricao_naturalidade
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'CandidatoCompleto':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        nome_urna = from_str(obj.get("nomeUrna"))
        numero = from_int(obj.get("numero"))
        id_candidato_superior = from_int(obj.get("idCandidatoSuperior"))
        nome_completo = from_str(obj.get("nomeCompleto"))
        descricao_sexo = from_str(obj.get("descricaoSexo"))
        data_de_nascimento = from_datetime(obj.get("dataDeNascimento"))
        titulo_eleitor = from_str(obj.get("tituloEleitor"))
        cpf = from_str(obj.get("cpf"))
        descricao_estado_civil = from_str(obj.get("descricaoEstadoCivil"))
        descricao_cor_raca = from_str(obj.get("descricaoCorRaca"))
        descricao_situacao = from_str(obj.get("descricaoSituacao"))
        nacionalidade = from_str(obj.get("nacionalidade"))
        grau_instrucao = from_str(obj.get("grauInstrucao"))
        ocupacao = from_str(obj.get("ocupacao"))
        gasto_campanha1_t = from_float(obj.get("gastoCampanha1T"))
        gasto_campanha2_t = from_float(obj.get("gastoCampanha2T"))
        sg_uf_nascimento = from_str(obj.get("sgUfNascimento"))
        nome_municipio_nascimento = from_str(
            obj.get("nomeMunicipioNascimento"))
        local_candidatura = from_str(obj.get("localCandidatura"))
        uf_candidatura = int(from_str(obj.get("ufCandidatura")))
        uf_superior_candidatura = from_str(obj.get("ufSuperiorCandidatura"))
        data_ultima_atualizacao = from_datetime(
            obj.get("dataUltimaAtualizacao"))
        foto_url = from_str(obj.get("fotoUrl"))
        foto_data_ultima_atualizacao = from_datetime(
            obj.get("fotoDataUltimaAtualizacao"))
        descricao_totalizacao = from_str(obj.get("descricaoTotalizacao"))
        nome_coligacao = from_str(obj.get("nomeColigacao"))
        composicao_coligacao = from_str(obj.get("composicaoColigacao"))
        descricao_tipo_drap = from_str(obj.get("descricaoTipoDrap"))
        numero_processo_drap = from_str(obj.get("numeroProcessoDrap"))
        numero_processo_drap_encrypt = from_str(
            obj.get("numeroProcessoDrapEncrypt"))
        numero_processo = from_str(obj.get("numeroProcesso"))
        numero_processo_encrypt = from_str(obj.get("numeroProcessoEncrypt"))
        numero_processo_prest_contas = from_str(
            obj.get("numeroProcessoPrestContas"))
        numero_processo_prest_contas_encrypt = from_str(
            obj.get("numeroProcessoPrestContasEncrypt"))
        numero_protocolo = from_int(from_str(obj.get("numeroProtocolo")))
        cargo = CargoDetail.from_dict(obj.get("cargo"))
        bens = from_list(Ben.from_dict, obj.get("bens"))
        total_de_bens = from_float(obj.get("totalDeBens"))
        vices = from_list(Vice.from_dict, obj.get("vices"))
        partido = Partido.from_dict(obj.get("partido"))
        eleicao = Eleicao.from_dict(obj.get("eleicao"))
        emails = from_list(from_str, obj.get("emails"))
        sites = from_list(lambda x: x, obj.get("sites"))
        arquivos = from_list(Arquivo.from_dict, obj.get("arquivos"))
        eleicoes_anteriores = from_list(
            EleicoesAnteriore.from_dict, obj.get("eleicoesAnteriores"))
        substituto = Substituto.from_dict(obj.get("substituto"))
        motivos = from_list(from_str, obj.get("motivos"))
        codigo_situacao_candidato = from_int(
            obj.get("codigoSituacaoCandidato"))
        descricao_situacao_candidato = from_str(
            obj.get("descricaoSituacaoCandidato"))
        is_candidato_inapto = from_bool(obj.get("isCandidatoInapto"))
        codigo_situacao_partido = from_str(obj.get("codigoSituacaoPartido"))
        descricao_situacao_partido = from_str(
            obj.get("descricaoSituacaoPartido"))
        is_cand_fechado = from_bool(obj.get("isCandFechado"))
        cnpjcampanha = from_str(obj.get("cnpjcampanha"))
        gasto_campanha = from_float(obj.get("gastoCampanha"))
        st_substituido = from_bool(obj.get("st_SUBSTITUIDO"))
        st_motivo_ficha_limpa = from_bool(obj.get("st_MOTIVO_FICHA_LIMPA"))
        st_motivo_abuso_poder = from_bool(obj.get("st_MOTIVO_ABUSO_PODER"))
        st_motivo_compra_voto = from_bool(obj.get("st_MOTIVO_COMPRA_VOTO"))
        st_motivo_conduta_vedada = from_bool(
            obj.get("st_MOTIVO_CONDUTA_VEDADA"))
        st_motivo_gasto_ilicito = from_bool(obj.get("st_MOTIVO_GASTO_ILICITO"))
        ds_motivo_outros = from_str(obj.get("ds_MOTIVO_OUTROS"))
        st_motivo_ausencia_requisito = from_bool(
            obj.get("st_MOTIVO_AUSENCIA_REQUISITO"))
        st_motivo_ind_partido = from_bool(obj.get("st_MOTIVO_IND_PARTIDO"))
        st_divulga = from_bool(obj.get("st_DIVULGA"))
        st_divulga_bens = from_bool(obj.get("st_DIVULGA_BENS"))
        st_reeleicao = from_bool(obj.get("st_REELEICAO"))
        st_divulga_arquivos = from_bool(obj.get("st_DIVULGA_ARQUIVOS"))
        descricao_naturalidade = from_str(obj.get("descricaoNaturalidade"))
        url = from_str(obj.get("url"))
        return CandidatoCompleto(id, nome_urna, numero, id_candidato_superior, nome_completo, descricao_sexo, data_de_nascimento, titulo_eleitor, cpf, descricao_estado_civil, descricao_cor_raca, descricao_situacao, nacionalidade, grau_instrucao, ocupacao, gasto_campanha1_t, gasto_campanha2_t, sg_uf_nascimento, nome_municipio_nascimento, local_candidatura, uf_candidatura, uf_superior_candidatura, data_ultima_atualizacao, foto_url, foto_data_ultima_atualizacao, descricao_totalizacao, nome_coligacao, composicao_coligacao, descricao_tipo_drap, numero_processo_drap, numero_processo_drap_encrypt, numero_processo, numero_processo_encrypt, numero_processo_prest_contas, numero_processo_prest_contas_encrypt, numero_protocolo, cargo, bens, total_de_bens, vices, partido, eleicao, emails, sites, arquivos, eleicoes_anteriores, substituto, motivos, codigo_situacao_candidato, descricao_situacao_candidato, is_candidato_inapto, codigo_situacao_partido, descricao_situacao_partido, is_cand_fechado, cnpjcampanha, gasto_campanha, st_substituido, st_motivo_ficha_limpa, st_motivo_abuso_poder, st_motivo_compra_voto, st_motivo_conduta_vedada, st_motivo_gasto_ilicito, ds_motivo_outros, st_motivo_ausencia_requisito, st_motivo_ind_partido, st_divulga, st_divulga_bens, st_reeleicao, st_divulga_arquivos, descricao_naturalidade, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["nomeUrna"] = from_str(self.nome_urna)
        result["numero"] = from_int(self.numero)
        result["idCandidatoSuperior"] = from_int(self.id_candidato_superior)
        result["nomeCompleto"] = from_str(self.nome_completo)
        result["descricaoSexo"] = from_str(self.descricao_sexo)
        result["dataDeNascimento"] = self.data_de_nascimento.isoformat()
        result["tituloEleitor"] = from_str(self.titulo_eleitor)
        result["cpf"] = from_str(self.cpf)
        result["descricaoEstadoCivil"] = from_str(self.descricao_estado_civil)
        result["descricaoCorRaca"] = from_str(self.descricao_cor_raca)
        result["descricaoSituacao"] = from_str(self.descricao_situacao)
        result["nacionalidade"] = from_str(self.nacionalidade)
        result["grauInstrucao"] = from_str(self.grau_instrucao)
        result["ocupacao"] = from_str(self.ocupacao)
        result["gastoCampanha1T"] = to_float(self.gasto_campanha1_t)
        result["gastoCampanha2T"] = from_int(self.gasto_campanha2_t)
        result["sgUfNascimento"] = from_str(self.sg_uf_nascimento)
        result["nomeMunicipioNascimento"] = from_str(
            self.nome_municipio_nascimento)
        result["localCandidatura"] = from_str(self.local_candidatura)
        result["ufCandidatura"] = from_str(str(self.uf_candidatura))
        result["ufSuperiorCandidatura"] = from_str(
            self.uf_superior_candidatura)
        result["dataUltimaAtualizacao"] = self.data_ultima_atualizacao.isoformat()
        result["fotoUrl"] = from_str(self.foto_url)
        result["fotoDataUltimaAtualizacao"] = self.foto_data_ultima_atualizacao.isoformat()
        result["descricaoTotalizacao"] = from_str(self.descricao_totalizacao)
        result["nomeColigacao"] = from_str(self.nome_coligacao)
        result["composicaoColigacao"] = from_str(self.composicao_coligacao)
        result["descricaoTipoDrap"] = from_str(self.descricao_tipo_drap)
        result["numeroProcessoDrap"] = from_str(self.numero_processo_drap)
        result["numeroProcessoDrapEncrypt"] = from_str(
            self.numero_processo_drap_encrypt)
        result["numeroProcesso"] = from_str(self.numero_processo)
        result["numeroProcessoEncrypt"] = from_str(
            self.numero_processo_encrypt)
        result["numeroProcessoPrestContas"] = from_none(
            self.numero_processo_prest_contas)
        result["numeroProcessoPrestContasEncrypt"] = from_none(
            self.numero_processo_prest_contas_encrypt)
        result["numeroProtocolo"] = from_str(str(self.numero_protocolo))
        result["cargo"] = to_class(CargoDetail, self.cargo)
        result["bens"] = from_list(lambda x: to_class(Ben, x), self.bens)
        result["totalDeBens"] = from_int(self.total_de_bens)
        result["vices"] = from_list(lambda x: to_class(Vice, x), self.vices)
        result["partido"] = to_class(Partido, self.partido)
        result["eleicao"] = to_class(Eleicao, self.eleicao)
        result["emails"] = from_list(from_str, self.emails)
        result["sites"] = from_list(lambda x: x, self.sites)
        result["arquivos"] = from_list(
            lambda x: to_class(Arquivo, x), self.arquivos)
        result["eleicoesAnteriores"] = from_list(lambda x: to_class(
            EleicoesAnteriore, x), self.eleicoes_anteriores)
        result["substituto"] = from_none(self.substituto)
        result["motivos"] = from_none(self.motivos)
        result["codigoSituacaoCandidato"] = from_int(
            self.codigo_situacao_candidato)
        result["descricaoSituacaoCandidato"] = from_none(
            self.descricao_situacao_candidato)
        result["isCandidatoInapto"] = from_bool(self.is_candidato_inapto)
        result["codigoSituacaoPartido"] = from_str(
            self.codigo_situacao_partido)
        result["descricaoSituacaoPartido"] = from_str(
            self.descricao_situacao_partido)
        result["isCandFechado"] = from_bool(self.is_cand_fechado)
        result["cnpjcampanha"] = from_str(self.cnpjcampanha)
        result["gastoCampanha"] = to_float(self.gasto_campanha)
        result["st_SUBSTITUIDO"] = from_bool(self.st_substituido)
        result["st_MOTIVO_FICHA_LIMPA"] = from_bool(self.st_motivo_ficha_limpa)
        result["st_MOTIVO_ABUSO_PODER"] = from_bool(self.st_motivo_abuso_poder)
        result["st_MOTIVO_COMPRA_VOTO"] = from_bool(self.st_motivo_compra_voto)
        result["st_MOTIVO_CONDUTA_VEDADA"] = from_bool(
            self.st_motivo_conduta_vedada)
        result["st_MOTIVO_GASTO_ILICITO"] = from_bool(
            self.st_motivo_gasto_ilicito)
        result["ds_MOTIVO_OUTROS"] = from_none(self.ds_motivo_outros)
        result["st_MOTIVO_AUSENCIA_REQUISITO"] = from_bool(
            self.st_motivo_ausencia_requisito)
        result["st_MOTIVO_IND_PARTIDO"] = from_bool(self.st_motivo_ind_partido)
        result["st_DIVULGA"] = from_bool(self.st_divulga)
        result["st_DIVULGA_BENS"] = from_bool(self.st_divulga_bens)
        result["st_REELEICAO"] = from_bool(self.st_reeleicao)
        result["st_DIVULGA_ARQUIVOS"] = from_bool(self.st_divulga_arquivos)
        result["descricaoNaturalidade"] = from_str(self.descricao_naturalidade)
        return result


def welcome9_from_dict(s: Any) -> CandidatoCompleto:
    return CandidatoCompleto.from_dict(s)


def welcome9_to_dict(x: CandidatoCompleto) -> Any:
    return to_class(CandidatoCompleto, x)
