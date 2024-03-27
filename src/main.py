import json
import requests
import pandas as pd

from models.eleicao_model import Eleicao
from models.candidato_completo_model import CandidatoCompleto
from models.candidato_model import Candidato, CandidatoDetail
from models.cargo_model import Cargo
from models.estado_municipio_model import EstadoMunicipio

from repository.database import import_data
from utils.constants import SCHEMA


def get_url_cargo(url_cargo, codigo_municipio):
    """
    Função para retorna a url tratada do cargo
    """
    return f"{url_cargo}{codigo_municipio}/cargos"


def get_url_candidato(url_candidato, codigo_municipio, id_eleicao, codigo_cargo):
    """
    Função para retorna a url tratada do candidato
    """
    return f"{url_candidato}{codigo_municipio}/{id_eleicao}/{codigo_cargo}/candidatos"


def get_url_candidato_completo(url_candidato_completo, codigo_municipio, id_eleicao, id_candidato):
    """
    Função para retorna a url tratada do candidato completo
    """
    return f"{url_candidato_completo}{codigo_municipio}/{id_eleicao}/candidato/{id_candidato}"


def get_eleicoes(url_eleicao):
    res_eleicoes = json.loads(requests.get(url_eleicao).text)

    eleicoes = []
    for res in res_eleicoes:
        if res.get("nomeEleicao") != "Eleições Municipais 2020 - AP":
            eleicoes.append(Eleicao.from_dict(res))
    return eleicoes


def escreve_db(schema):
    # Ler dados gravados
    df_eleicoes = pd.read_excel(
        'dados_combinados.xlsx', sheet_name='Dados Principais')
    df_eleicoes_ant = pd.read_excel(
        'dados_combinados.xlsx', sheet_name='Eleições Anteriores')
    df_arquivos = pd.read_excel('dados_combinados.xlsx', sheet_name='Arquivos')
    df_sites = pd.read_excel('dados_combinados.xlsx', sheet_name='Sites')

    import_data(df_eleicoes, schema, "eleicao")
    import_data(df_eleicoes_ant, schema, "eleicao_anterior")
    import_data(df_arquivos, schema, "eleicao_arquivo")
    import_data(df_sites, schema, "eleicao_site")


def escreve_df(lista_candidato_completo: list[CandidatoCompleto], ano_eleicao: int, lista_candidato_erro: list[CandidatoDetail]):

    # Criação do DataFrame principal
    df = pd.DataFrame(
        data=[(item.nome_completo, item.cargo.nome, item.local_candidatura, item.uf_candidatura, item.cnpjcampanha, item.descricao_sexo, item.descricao_cor_raca, item.nacionalidade, item.grau_instrucao, item.gasto_campanha1_t, item.gasto_campanha2_t,
               item.numero_processo_drap, item.numero_processo,  item.numero_processo_prest_contas, item.id, item.numero)
              for item in lista_candidato_completo],
        columns=["nome_completo", "cargo", "localCandidatura", "ufCandidatura", "cnpjcampanha", "descricaoSexo", "descricaoCorRaca", "nacionalidade", "grauInstrucao", "gastoCampanha1T", "gastoCampanha2T",
                 "numeroProcessoDrap", "numeroProcesso", "numeroProcessoPrestContas", "id", "numero"])
    # df_erro = pd.DataFrame(
    #     data=[(item.nome_completo, item.cargo.nome, item.local_candidatura, item.uf_candidatura, item.cnpjcampanha, item.descricao_sexo, item.descricao_cor_raca, item.nacionalidade, item.grau_instrucao, item.gasto_campanha1_t, item.gasto_campanha2_t,
    #            item.numero_processo_drap, item.numero_processo,  item.numero_processo_prest_contas, item.id, item.numero)
    #           for item in lista_candidato_erro],
    #     columns=["nome_completo", "cargo", "localCandidatura", "ufCandidatura", "cnpjcampanha", "descricaoSexo", "descricaoCorRaca", "nacionalidade", "grauInstrucao", "gastoCampanha1T", "gastoCampanha2T",
    #              "numeroProcessoDrap", "numeroProcesso", "numeroProcessoPrestContas", "id", "numero"])

    df["anoEleicao"] = ano_eleicao
    # df_erro["anoEleicao"] = ano_eleicao

    # Criação do DataFrame das eleições anteriores
    eleicoes_anteriores = []
    arquivos = []
    sites = []
    for item in lista_candidato_completo:

        url = f"https://divulgacandcontas.tse.jus.br/dados/{ano_eleicao}/{sigla_estado}/{item.uf_candidatura}/{item.codigo_situacao_candidato}/{item.id}/"

        for eleicao in item.eleicoes_anteriores:
            eleicoes_anteriores.append([item.id, eleicao.nr_ano, eleicao.cargo, eleicao.local,
                                        eleicao.partido, eleicao.situacao_totalizacao, eleicao.tx_link, eleicao.id, ano_eleicao])
        for arquivo in item.arquivos:

            tipoArquivo = ""

            # Case tipos
            match arquivo.cod_tipo:
                case 5:
                    tipoArquivo = "Proposta de Governo"
                case 11:
                    tipoArquivo = "Certidão criminal da Justiça Federal de 1º grau"
                case 12:
                    tipoArquivo = "Certidão criminal da Justiça Federal de 2º grau"
                case 13:
                    tipoArquivo = "Certidão criminal da Justiça Estadual de 1º grau"
                case 14:
                    tipoArquivo = "Certidão criminal da Justiça Estadual de 2º grau"
                case 15:
                    tipoArquivo = "Certidão criminal de foro por prerrogativa de função"

            arquivos.append([item.id, url + arquivo.nome,
                            arquivo.id_arquivo, arquivo.cod_tipo, tipoArquivo, ano_eleicao])

        for site in item.sites:
            sites.append([item.id, site, ano_eleicao])

    df_eleicoes = pd.DataFrame(
        data=eleicoes_anteriores,
        columns=["idUsuario", "nrAno", "cargo", "local", "partido", "situacaoTotalizacao", "txLink", "idEleicao", "anoEleicao"])

    df_arquivos = pd.DataFrame(
        data=arquivos,
        columns=["idUsuario", "url", "idArquivo", "codTipo", "tipoArquivo", "anoEleicao"])

    df_sites = pd.DataFrame(
        data=sites,
        columns=["idUsuario", "url", "anoEleicao"])

    # Ler dados gravados
    df_excel = pd.read_excel('dados_combinados.xlsx',
                             sheet_name='Dados Principais')
    df_eleicoes_excel = pd.read_excel(
        'dados_combinados.xlsx', sheet_name='Eleições Anteriores')
    df_arquivos_excel = pd.read_excel(
        'dados_combinados.xlsx', sheet_name='Arquivos')
    df_sites_excel = pd.read_excel('dados_combinados.xlsx', sheet_name='Sites')
    # df_erro_excel = pd.read_excel('dados_combinados.xlsx', sheet_name='Erros')

    # concat dfs
    df = pd.concat([df if not df.empty else None, df_excel])
    df_eleicoes = pd.concat(
        [df_eleicoes if not df_eleicoes.empty else None, df_eleicoes_excel])
    df_arquivos = pd.concat(
        [df_arquivos if not df_arquivos.empty else None, df_arquivos_excel])
    df_sites = pd.concat(
        [df_sites if not df_sites.empty else None, df_sites_excel])
    # df_erro = pd.concat(
    #     [df_erro if not df_erro.empty else None, df_erro_excel])

    # Salvando ambos os DataFrames em diferentes abas no mesmo arquivo Excel
    with pd.ExcelWriter('dados_combinados.xlsx') as writer:
        df.to_excel(writer, index=False, sheet_name='Dados Principais')
        df_eleicoes.to_excel(writer, index=False,
                             sheet_name='Eleições Anteriores')
        df_arquivos.to_excel(writer, index=False, sheet_name='Arquivos')
        df_sites.to_excel(writer, index=False, sheet_name='Sites')
        # df_erro.to_excel(writer, index=False, sheet_name='Sites')

    print(lista_erro_candidato_completo)


base_url = "https://divulgacandcontas.tse.jus.br/divulga/rest/v1/"
url_eleicao = f"{base_url}eleicao/ordinarias"


# Lista todos anos das eleições
eleicoes: list[Eleicao] = get_eleicoes(url_eleicao)

extrair_novamente = str(input(
    "\nDeseja extrair dados do site? (S/N) - se NÃO, o código irá considerar a planilha salva - ")).upper()

if extrair_novamente == 'S':

    print("\nLista de eleições disponiveis para extração (RJ):")
    for idx, eleicao in enumerate(eleicoes):
        print(idx, "-", eleicao.ano)

    try:
        idx_selecionado = int(input("Digite o indice do ano: "))
    except:
        print("opção invalida!")
        exit()

    ano_eleicao = eleicoes[idx_selecionado].ano
    id_eleicao = eleicoes[idx_selecionado].id
    sigla_estado = "RJ"

    url_municipio = f"{base_url}eleicao/buscar/{sigla_estado}/{id_eleicao}/municipios"
    url_base_cargo = f"{base_url}eleicao/listar/municipios/{id_eleicao}/"
    url_base_candidato = f"{base_url}candidatura/listar/{ano_eleicao}/"
    url_base_candidato_completo = f"{base_url}candidatura/buscar/{ano_eleicao}/"
    lista_candidato_completo: list[CandidatoCompleto] = []
    lista_erro_candidato_completo: list[CandidatoDetail] = []

    res_municipios = requests.get(url_municipio)

    estados_municipios = EstadoMunicipio.from_dict(
        json.loads(res_municipios.text))

    # Lista de municipios salvos
    df_excel = pd.read_excel('dados_combinados.xlsx',
                             sheet_name='Dados Principais')
    list_municipios = df_excel["localCandidatura"].drop_duplicates().tolist()

    # Primeiro loop para pegar todos municipios do estado
    for index, municipio in enumerate(estados_municipios.municipios):

        # if index > 3:
        #     break

        # Pula municipios salvos
        if municipio.nome in list_municipios:
            continue

        print(f"{index} de {len(estados_municipios.municipios)}")

        print(municipio.codigo, municipio.nome)

        # Localiza todos os cargos de acordo com o municipio e eleição
        url_cargo = get_url_cargo(url_base_cargo, municipio.codigo)

        res_cargos = requests.get(url_cargo)

        cargos = Cargo.from_dict(json.loads(res_cargos.text))

        # Percore cada cargo de cada municipio para localizar os candidatos
        for index, cargo in enumerate(cargos.cargos):

            # if index > 3:
            #     break

            print(f"{index} de {len(cargos.cargos)}")
            print(cargo.codigo, cargo.nome)

            # Localiza todos candidados de acordo com os cargos
            url_candidato = get_url_candidato(
                url_base_candidato, municipio.codigo, id_eleicao, cargo.codigo)

            res_candidatos = requests.get(url_candidato)

            candidatos = Candidato.from_dict(json.loads(res_candidatos.text))

            # Percore cada candidado para encontrar seu ID para pegar os dados completos
            for index, candidato in enumerate(candidatos.candidatos):

                # if index > 3:
                #     break

                print(f"{index} de {len(candidatos.candidatos)}")

                try:
                    print(candidato.id, candidato.nome_completo)

                    if candidato.nome_completo == "(DADOS NÃO DIVULGADOS)":
                        continue

                    # Captura todas informações detalhadas do canditado
                    url_candidatos_completo = get_url_candidato_completo(
                        url_base_candidato_completo, municipio.codigo, id_eleicao, candidato.id)  # candidato.id)
                    print(url_candidatos_completo)
                    res_candidatos_completo = requests.get(
                        url_candidatos_completo)
                    dic = json.loads(res_candidatos_completo.text)
                    dic["url"] = url_candidatos_completo
                    candidato_completo = CandidatoCompleto.from_dict(dic)
                    lista_candidato_completo.append(candidato_completo)

                    print(candidato_completo.id, candidato_completo.numero,
                          candidato_completo.nome_urna, candidato_completo.nome_completo)

                except Exception as e:
                    print(e)
                    lista_erro_candidato_completo.append(candidato)

        # Escreve no excel após buscar os dados de cada municipio
        escreve_df(lista_candidato_completo, ano_eleicao,
                   lista_erro_candidato_completo)
        lista_candidato_completo = []
        lista_erro_candidato_completo = []

    escreve_db(SCHEMA)

elif extrair_novamente == 'N':
    print("dados da planilha")
    escreve_db(SCHEMA)

else:
    print("opção invalida!")
