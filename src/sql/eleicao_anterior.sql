CREATE TABLE if not exists eleicao_anterior (
	idUsuario BIGINT
	,nrAno INT
	,cargo VARCHAR(50)
	,local VARCHAR(50)
	,partido VARCHAR(20)
	,situacaoTotalizacao VARCHAR(100)
	,txLink VARCHAR(255)
	,idEleicao VARCHAR(20)
	,anoEleicao INT
);