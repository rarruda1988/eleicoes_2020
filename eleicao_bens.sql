CREATE TABLE if not exists eleicao_bens (
	idUsuario BIGINT
	,ordem INT
	,descricao VARCHAR(1000)
	,descricao_de_tipo_de_bem VARCHAR(255)
	,valor NUMERIC
	,data_ultima_atualizacao TIMESTAMP
	,anoEleicao INT
);