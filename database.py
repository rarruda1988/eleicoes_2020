import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


def get_engine():
    try:
        load_dotenv()
        return create_engine(os.getenv("DB_URL"))
    except Exception as e:
        raise e


def create_tables(engine):
    try:

        with engine.connect() as conn:
            
            with open("src/sql/eleicao.sql") as file:
                query = text(file.read())
                conn.execute(query)
                conn.commit()
            
            with open("src/sql/eleicao_anterior.sql") as file:
                query = text(file.read())
                conn.execute(query)
                conn.commit()
                
            with open("src/sql/eleicao_arquivo.sql") as file:
                query = text(file.read())
                conn.execute(query)
                conn.commit()
                
            with open("src/sql/eleicao_site.sql") as file:
                query = text(file.read())
                conn.execute(query)
                conn.commit()
                
            with open("src/sql/eleicao_bens.sql") as file:
                query = text(file.read())
                conn.execute(query)
                conn.commit()
                
    except Exception as e:
        raise e

def insert_eleicao(df, engine, schema, table):

    try:
        
        df.columns = df.columns.str.lower()
        
        if df.empty:
            print(f"""Planilha vazia, sem dados para insert""")
            return None
        
        anos = df["anoeleicao"].drop_duplicates().to_list()


        with engine.connect() as conn:
            
            for ano in anos:
                
                print(f"Deletando dados da tabela {schema}.{table} do ano de eleição:", ano)
                
                # deleta dados do dataframe tratado na tabela
                result = conn.execute(text(f"""DELETE FROM {schema}.{table} WHERE anoEleicao = {ano}"""))

            # Commita deletes
            conn.commit()
            
            print(f"Inserindo dados na tabela {schema}.{table}")

            # Inseri dados do dataframe tratado na tabela
            df.to_sql(name=table,
                      schema=schema,
                      con=conn,
                      if_exists='append',
                      index=False,
                      )

    except Exception as e:
        raise e



def import_data(df, schema, table):

    engine = get_engine()
    
    # Cria tabelas
    create_tables(engine)

    # Inseri dados na tabela
    insert_eleicao(df, engine, schema, table)


if __name__ == "__main__":

    # Ler dados gravados
    df_eleicoes = pd.read_excel('dados_combinados.xlsx', sheet_name='Dados Principais')
    df_eleicoes_ant = pd.read_excel('dados_combinados.xlsx', sheet_name='Eleições Anteriores')
    df_arquivos = pd.read_excel('dados_combinados.xlsx', sheet_name='Arquivos')
    df_sites = pd.read_excel('dados_combinados.xlsx', sheet_name='Sites')
    df_bens = pd.read_excel('dados_combinados.xlsx', sheet_name='Bens')

    # Database
    SCHEMA = "public"
    

    import_data(df_eleicoes, SCHEMA, "eleicao")
    import_data(df_eleicoes_ant, SCHEMA, "eleicao_anterior")
    import_data(df_arquivos, SCHEMA, "eleicao_arquivo")
    import_data(df_sites, SCHEMA, "eleicao_site")
    import_data(df_bens, SCHEMA, "eleicao_bens")
    
