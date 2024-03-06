# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome10_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Type, cast, Callable

from models.cargo_model import CargoDetail

T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    if not x:
        return ""
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]

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
        result["nomeEleicao"] = from_none(self.nome_eleicao)
        result["tipoEleicao"] = from_none(self.tipo_eleicao)
        result["turno"] = from_none(self.turno)
        result["tipoAbrangencia"] = from_none(self.tipo_abrangencia)
        result["dataEleicao"] = from_none(self.data_eleicao)
        result["codSituacaoEleicao"] = from_none(self.cod_situacao_eleicao)
        result["descricaoSituacaoEleicao"] = from_none(self.descricao_situacao_eleicao)
        result["descricaoEleicao"] = from_str(str(self.descricao_eleicao))
        return result


class Partido:
    numero: int
    sigla: str
    nome: None

    def __init__(self, numero: int, sigla: str, nome: None) -> None:
        self.numero = numero
        self.sigla = sigla
        self.nome = nome

    @staticmethod
    def from_dict(obj: Any) -> 'Partido':
        assert isinstance(obj, dict)
        numero = from_int(obj.get("numero"))
        sigla = from_str(obj.get("sigla"))
        nome = from_none(obj.get("nome"))
        return Partido(numero, sigla, nome)

    def to_dict(self) -> dict:
        result: dict = {}
        result["numero"] = from_int(self.numero)
        result["sigla"] = from_str(self.sigla)
        result["nome"] = from_none(self.nome)
        return result


class CandidatoDetail:
    id: int
    nome_urna: str
    numero: int
    id_candidato_superior: None
    nome_completo: str
    descricao_sexo: None
    data_de_nascimento: None
    titulo_eleitor: None
    cpf: None
    descricao_estado_civil: None
    descricao_cor_raca: None
    descricao_situacao: str
    nacionalidade: None
    grau_instrucao: None
    ocupacao: None
    gasto_campanha1_t: None
    gasto_campanha2_t: None
    sg_uf_nascimento: None
    nome_municipio_nascimento: None
    local_candidatura: None
    uf_candidatura: None
    uf_superior_candidatura: None
    data_ultima_atualizacao: None
    foto_url: None
    foto_data_ultima_atualizacao: None
    descricao_totalizacao: str
    nome_coligacao: str
    composicao_coligacao: None
    descricao_tipo_drap: None
    numero_processo_drap: None
    numero_processo_drap_encrypt: None
    numero_processo: None
    numero_processo_encrypt: None
    numero_processo_prest_contas: None
    numero_processo_prest_contas_encrypt: None
    numero_protocolo: None
    cargo: CargoDetail
    bens: None
    total_de_bens: None
    vices: None
    partido: Partido
    eleicao: Eleicao
    emails: None
    sites: None
    arquivos: None
    eleicoes_anteriores: None
    substituto: None
    motivos: None
    codigo_situacao_candidato: None
    descricao_situacao_candidato: None
    is_candidato_inapto: None
    codigo_situacao_partido: None
    descricao_situacao_partido: None
    is_cand_fechado: None
    descricao_naturalidade: str
    st_motivo_ficha_limpa: None
    st_motivo_abuso_poder: None
    st_motivo_compra_voto: None
    st_motivo_conduta_vedada: None
    st_motivo_gasto_ilicito: None
    ds_motivo_outros: None
    st_motivo_ausencia_requisito: None
    st_motivo_ind_partido: None
    st_divulga: None
    st_divulga_bens: None
    st_reeleicao: bool
    st_divulga_arquivos: None
    st_substituido: None
    cnpjcampanha: None
    gasto_campanha: float

    def __init__(self, id: int, nome_urna: str, numero: int, id_candidato_superior: None, nome_completo: str, descricao_sexo: None, data_de_nascimento: None, titulo_eleitor: None, cpf: None, descricao_estado_civil: None, descricao_cor_raca: None, descricao_situacao: str, nacionalidade: None, grau_instrucao: None, ocupacao: None, gasto_campanha1_t: None, gasto_campanha2_t: None, sg_uf_nascimento: None, nome_municipio_nascimento: None, local_candidatura: None, uf_candidatura: None, uf_superior_candidatura: None, data_ultima_atualizacao: None, foto_url: None, foto_data_ultima_atualizacao: None, descricao_totalizacao: str, nome_coligacao: str, composicao_coligacao: None, descricao_tipo_drap: None, numero_processo_drap: None, numero_processo_drap_encrypt: None, numero_processo: None, numero_processo_encrypt: None, numero_processo_prest_contas: None, numero_processo_prest_contas_encrypt: None, numero_protocolo: None, cargo: CargoDetail, bens: None, total_de_bens: None, vices: None, partido: Partido, eleicao: Eleicao, emails: None, sites: None, arquivos: None, eleicoes_anteriores: None, substituto: None, motivos: None, codigo_situacao_candidato: None, descricao_situacao_candidato: None, is_candidato_inapto: None, codigo_situacao_partido: None, descricao_situacao_partido: None, is_cand_fechado: None, descricao_naturalidade: str, st_motivo_ficha_limpa: None, st_motivo_abuso_poder: None, st_motivo_compra_voto: None, st_motivo_conduta_vedada: None, st_motivo_gasto_ilicito: None, ds_motivo_outros: None, st_motivo_ausencia_requisito: None, st_motivo_ind_partido: None, st_divulga: None, st_divulga_bens: None, st_reeleicao: bool, st_divulga_arquivos: None, st_substituido: None, cnpjcampanha: None, gasto_campanha: float) -> None:
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
        self.descricao_naturalidade = descricao_naturalidade
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
        self.st_substituido = st_substituido
        self.cnpjcampanha = cnpjcampanha
        self.gasto_campanha = gasto_campanha

    @staticmethod
    def from_dict(obj: Any) -> 'CandidatoDetail':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        nome_urna = from_str(obj.get("nomeUrna"))
        numero = from_int(obj.get("numero"))
        id_candidato_superior = from_none(obj.get("idCandidatoSuperior"))
        nome_completo = from_str(obj.get("nomeCompleto"))
        descricao_sexo = from_none(obj.get("descricaoSexo"))
        data_de_nascimento = from_none(obj.get("dataDeNascimento"))
        titulo_eleitor = from_none(obj.get("tituloEleitor"))
        cpf = from_none(obj.get("cpf"))
        descricao_estado_civil = from_none(obj.get("descricaoEstadoCivil"))
        descricao_cor_raca = from_none(obj.get("descricaoCorRaca"))
        descricao_situacao = from_str(obj.get("descricaoSituacao"))
        nacionalidade = from_none(obj.get("nacionalidade"))
        grau_instrucao = from_none(obj.get("grauInstrucao"))
        ocupacao = from_none(obj.get("ocupacao"))
        gasto_campanha1_t = from_none(obj.get("gastoCampanha1T"))
        gasto_campanha2_t = from_none(obj.get("gastoCampanha2T"))
        sg_uf_nascimento = from_none(obj.get("sgUfNascimento"))
        nome_municipio_nascimento = from_none(obj.get("nomeMunicipioNascimento"))
        local_candidatura = from_none(obj.get("localCandidatura"))
        uf_candidatura = from_none(obj.get("ufCandidatura"))
        uf_superior_candidatura = from_none(obj.get("ufSuperiorCandidatura"))
        data_ultima_atualizacao = from_none(obj.get("dataUltimaAtualizacao"))
        foto_url = from_none(obj.get("fotoUrl"))
        foto_data_ultima_atualizacao = from_none(obj.get("fotoDataUltimaAtualizacao"))
        descricao_totalizacao = from_str(obj.get("descricaoTotalizacao"))
        nome_coligacao = from_str(obj.get("nomeColigacao"))
        composicao_coligacao = from_none(obj.get("composicaoColigacao"))
        descricao_tipo_drap = from_none(obj.get("descricaoTipoDrap"))
        numero_processo_drap = from_none(obj.get("numeroProcessoDrap"))
        numero_processo_drap_encrypt = from_none(obj.get("numeroProcessoDrapEncrypt"))
        numero_processo = from_none(obj.get("numeroProcesso"))
        numero_processo_encrypt = from_none(obj.get("numeroProcessoEncrypt"))
        numero_processo_prest_contas = from_none(obj.get("numeroProcessoPrestContas"))
        numero_processo_prest_contas_encrypt = from_none(obj.get("numeroProcessoPrestContasEncrypt"))
        numero_protocolo = from_none(obj.get("numeroProtocolo"))
        cargo = CargoDetail.from_dict(obj.get("cargo"))
        bens = from_none(obj.get("bens"))
        total_de_bens = from_none(obj.get("totalDeBens"))
        vices = from_none(obj.get("vices"))
        partido = Partido.from_dict(obj.get("partido"))
        eleicao = Eleicao.from_dict(obj.get("eleicao"))
        emails = from_none(obj.get("emails"))
        sites = from_none(obj.get("sites"))
        arquivos = from_none(obj.get("arquivos"))
        eleicoes_anteriores = from_none(obj.get("eleicoesAnteriores"))
        substituto = from_none(obj.get("substituto"))
        motivos = from_none(obj.get("motivos"))
        codigo_situacao_candidato = from_none(obj.get("codigoSituacaoCandidato"))
        descricao_situacao_candidato = from_none(obj.get("descricaoSituacaoCandidato"))
        is_candidato_inapto = from_none(obj.get("isCandidatoInapto"))
        codigo_situacao_partido = from_none(obj.get("codigoSituacaoPartido"))
        descricao_situacao_partido = from_none(obj.get("descricaoSituacaoPartido"))
        is_cand_fechado = from_none(obj.get("isCandFechado"))
        descricao_naturalidade = from_str(obj.get("descricaoNaturalidade"))
        st_motivo_ficha_limpa = from_none(obj.get("st_MOTIVO_FICHA_LIMPA"))
        st_motivo_abuso_poder = from_none(obj.get("st_MOTIVO_ABUSO_PODER"))
        st_motivo_compra_voto = from_none(obj.get("st_MOTIVO_COMPRA_VOTO"))
        st_motivo_conduta_vedada = from_none(obj.get("st_MOTIVO_CONDUTA_VEDADA"))
        st_motivo_gasto_ilicito = from_none(obj.get("st_MOTIVO_GASTO_ILICITO"))
        ds_motivo_outros = from_none(obj.get("ds_MOTIVO_OUTROS"))
        st_motivo_ausencia_requisito = from_none(obj.get("st_MOTIVO_AUSENCIA_REQUISITO"))
        st_motivo_ind_partido = from_none(obj.get("st_MOTIVO_IND_PARTIDO"))
        st_divulga = from_none(obj.get("st_DIVULGA"))
        st_divulga_bens = from_none(obj.get("st_DIVULGA_BENS"))
        st_reeleicao = from_bool(obj.get("st_REELEICAO"))
        st_divulga_arquivos = from_none(obj.get("st_DIVULGA_ARQUIVOS"))
        st_substituido = from_none(obj.get("st_SUBSTITUIDO"))
        cnpjcampanha = from_none(obj.get("cnpjcampanha"))
        gasto_campanha = from_float(obj.get("gastoCampanha"))
        return CandidatoDetail(id, nome_urna, numero, id_candidato_superior, nome_completo, descricao_sexo, data_de_nascimento, titulo_eleitor, cpf, descricao_estado_civil, descricao_cor_raca, descricao_situacao, nacionalidade, grau_instrucao, ocupacao, gasto_campanha1_t, gasto_campanha2_t, sg_uf_nascimento, nome_municipio_nascimento, local_candidatura, uf_candidatura, uf_superior_candidatura, data_ultima_atualizacao, foto_url, foto_data_ultima_atualizacao, descricao_totalizacao, nome_coligacao, composicao_coligacao, descricao_tipo_drap, numero_processo_drap, numero_processo_drap_encrypt, numero_processo, numero_processo_encrypt, numero_processo_prest_contas, numero_processo_prest_contas_encrypt, numero_protocolo, cargo, bens, total_de_bens, vices, partido, eleicao, emails, sites, arquivos, eleicoes_anteriores, substituto, motivos, codigo_situacao_candidato, descricao_situacao_candidato, is_candidato_inapto, codigo_situacao_partido, descricao_situacao_partido, is_cand_fechado, descricao_naturalidade, st_motivo_ficha_limpa, st_motivo_abuso_poder, st_motivo_compra_voto, st_motivo_conduta_vedada, st_motivo_gasto_ilicito, ds_motivo_outros, st_motivo_ausencia_requisito, st_motivo_ind_partido, st_divulga, st_divulga_bens, st_reeleicao, st_divulga_arquivos, st_substituido, cnpjcampanha, gasto_campanha)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["nomeUrna"] = from_str(self.nome_urna)
        result["numero"] = from_int(self.numero)
        result["idCandidatoSuperior"] = from_none(self.id_candidato_superior)
        result["nomeCompleto"] = from_str(self.nome_completo)
        result["descricaoSexo"] = from_none(self.descricao_sexo)
        result["dataDeNascimento"] = from_none(self.data_de_nascimento)
        result["tituloEleitor"] = from_none(self.titulo_eleitor)
        result["cpf"] = from_none(self.cpf)
        result["descricaoEstadoCivil"] = from_none(self.descricao_estado_civil)
        result["descricaoCorRaca"] = from_none(self.descricao_cor_raca)
        result["descricaoSituacao"] = from_str(self.descricao_situacao)
        result["nacionalidade"] = from_none(self.nacionalidade)
        result["grauInstrucao"] = from_none(self.grau_instrucao)
        result["ocupacao"] = from_none(self.ocupacao)
        result["gastoCampanha1T"] = from_none(self.gasto_campanha1_t)
        result["gastoCampanha2T"] = from_none(self.gasto_campanha2_t)
        result["sgUfNascimento"] = from_none(self.sg_uf_nascimento)
        result["nomeMunicipioNascimento"] = from_none(self.nome_municipio_nascimento)
        result["localCandidatura"] = from_none(self.local_candidatura)
        result["ufCandidatura"] = from_none(self.uf_candidatura)
        result["ufSuperiorCandidatura"] = from_none(self.uf_superior_candidatura)
        result["dataUltimaAtualizacao"] = from_none(self.data_ultima_atualizacao)
        result["fotoUrl"] = from_none(self.foto_url)
        result["fotoDataUltimaAtualizacao"] = from_none(self.foto_data_ultima_atualizacao)
        result["descricaoTotalizacao"] = from_str(self.descricao_totalizacao)
        result["nomeColigacao"] = from_str(self.nome_coligacao)
        result["composicaoColigacao"] = from_none(self.composicao_coligacao)
        result["descricaoTipoDrap"] = from_none(self.descricao_tipo_drap)
        result["numeroProcessoDrap"] = from_none(self.numero_processo_drap)
        result["numeroProcessoDrapEncrypt"] = from_none(self.numero_processo_drap_encrypt)
        result["numeroProcesso"] = from_none(self.numero_processo)
        result["numeroProcessoEncrypt"] = from_none(self.numero_processo_encrypt)
        result["numeroProcessoPrestContas"] = from_none(self.numero_processo_prest_contas)
        result["numeroProcessoPrestContasEncrypt"] = from_none(self.numero_processo_prest_contas_encrypt)
        result["numeroProtocolo"] = from_none(self.numero_protocolo)
        result["cargo"] = to_class(CargoDetail, self.cargo)
        result["bens"] = from_none(self.bens)
        result["totalDeBens"] = from_none(self.total_de_bens)
        result["vices"] = from_none(self.vices)
        result["partido"] = to_class(Partido, self.partido)
        result["eleicao"] = to_class(Eleicao, self.eleicao)
        result["emails"] = from_none(self.emails)
        result["sites"] = from_none(self.sites)
        result["arquivos"] = from_none(self.arquivos)
        result["eleicoesAnteriores"] = from_none(self.eleicoes_anteriores)
        result["substituto"] = from_none(self.substituto)
        result["motivos"] = from_none(self.motivos)
        result["codigoSituacaoCandidato"] = from_none(self.codigo_situacao_candidato)
        result["descricaoSituacaoCandidato"] = from_none(self.descricao_situacao_candidato)
        result["isCandidatoInapto"] = from_none(self.is_candidato_inapto)
        result["codigoSituacaoPartido"] = from_none(self.codigo_situacao_partido)
        result["descricaoSituacaoPartido"] = from_none(self.descricao_situacao_partido)
        result["isCandFechado"] = from_none(self.is_cand_fechado)
        result["descricaoNaturalidade"] = from_str(self.descricao_naturalidade)
        result["st_MOTIVO_FICHA_LIMPA"] = from_none(self.st_motivo_ficha_limpa)
        result["st_MOTIVO_ABUSO_PODER"] = from_none(self.st_motivo_abuso_poder)
        result["st_MOTIVO_COMPRA_VOTO"] = from_none(self.st_motivo_compra_voto)
        result["st_MOTIVO_CONDUTA_VEDADA"] = from_none(self.st_motivo_conduta_vedada)
        result["st_MOTIVO_GASTO_ILICITO"] = from_none(self.st_motivo_gasto_ilicito)
        result["ds_MOTIVO_OUTROS"] = from_none(self.ds_motivo_outros)
        result["st_MOTIVO_AUSENCIA_REQUISITO"] = from_none(self.st_motivo_ausencia_requisito)
        result["st_MOTIVO_IND_PARTIDO"] = from_none(self.st_motivo_ind_partido)
        result["st_DIVULGA"] = from_none(self.st_divulga)
        result["st_DIVULGA_BENS"] = from_none(self.st_divulga_bens)
        result["st_REELEICAO"] = from_bool(self.st_reeleicao)
        result["st_DIVULGA_ARQUIVOS"] = from_none(self.st_divulga_arquivos)
        result["st_SUBSTITUIDO"] = from_none(self.st_substituido)
        result["cnpjcampanha"] = from_none(self.cnpjcampanha)
        result["gastoCampanha"] = to_float(self.gasto_campanha)
        return result


class UnidadeEleitoral:
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
    def from_dict(obj: Any) -> 'UnidadeEleitoral':
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
        return UnidadeEleitoral(id, sigla, nome, regiao, cargos, diretorios, codigo, capital, estado)

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


class Candidato:
    unidade_eleitoral: UnidadeEleitoral
    cargo: CargoDetail
    candidatos: List[CandidatoDetail]

    def __init__(self, unidade_eleitoral: UnidadeEleitoral, cargo: CargoDetail, candidatos: List[CandidatoDetail]) -> None:
        self.unidade_eleitoral = unidade_eleitoral
        self.cargo = cargo
        self.candidatos = candidatos

    @staticmethod
    def from_dict(obj: Any) -> 'Candidato':
        assert isinstance(obj, dict)
        unidade_eleitoral = UnidadeEleitoral.from_dict(obj.get("unidadeEleitoral"))
        cargo = CargoDetail.from_dict(obj.get("cargo"))
        candidatos = from_list(CandidatoDetail.from_dict, obj.get("candidatos"))
        return Candidato(unidade_eleitoral, cargo, candidatos)

    def to_dict(self) -> dict:
        result: dict = {}
        result["unidadeEleitoral"] = to_class(UnidadeEleitoral, self.unidade_eleitoral)
        result["cargo"] = to_class(CargoDetail, self.cargo)
        result["candidatos"] = from_list(lambda x: to_class(CandidatoDetail, x), self.candidatos)
        return result


def welcome10_from_dict(s: Any) -> Candidato:
    return Candidato.from_dict(s)



def welcome10_to_dict(x: Candidato) -> Any:
    return to_class(Candidato, x)
