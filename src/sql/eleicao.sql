CREATE TABLE if not exists eleicao (
	nome_completo VARCHAR(150)
	,cargo VARCHAR(50)
	,localCandidatura VARCHAR(60)
	,ufCandidatura VARCHAR(50)
	,cnpjcampanha VARCHAR(20)
	,descricaoSexo VARCHAR(10)
	,descricaoCorRaca VARCHAR(20)
	,nacionalidade VARCHAR(50)
	,grauInstrucao VARCHAR(50)
	,gastoCampanha1T NUMERIC
	,gastoCampanha2T NUMERIC
	,numeroProcessoDrap VARCHAR(20)
	,numeroProcesso VARCHAR(20)
	,numeroProcessoPrestContas VARCHAR(20)
	,id BIGINT PRIMARY KEY
	,anoEleicao INT
);