DROP DATABASE IF EXISTS dados_pessoais;
CREATE DATABASE dados_pessoais;

-- CRIANDO A TABELA PESSOAS

USE dados_pessoais;

CREATE TABLE pessoas (
                      id INTEGER PRIMARY KEY AUTO_INCREMENT,
                      nome VARCHAR(255) NOT NULL,
                      idade VARCHAR(3) NOT NULL,
                      genero VARCHAR(20) NOT NULL,
                      nacionalidade VARCHAR(20),
                      estado_civil VARCHAR(20) NOT NULL,
                      nome_pai VARCHAR(255) NOT NULL,
                      nome_mae VARCHAR(255) NOT NULL
);


-- INSERÇÕES NO BANCO DE DADOS

INSERT INTO pessoas (nome, idade, genero, nacionalidade, estado_civil, nome_pai, nome_mae) VALUES
("Rogério Afonso Fonseca", "23" , "Masculino", "Argentino(a)", "Solteiro(a)","Hernandes Hermoso Carlos", "Celestina Ferreira Abalante"),
("Roberta Gonçálves Pereira", "31" , "Feminino", "Brasileiro(a)", "Casado(a)","Paulo Ferreira Gonçálves", "Maria Valéria Pereira da Silva "),
("Valdecir Bruno de Oliveira", "55" , "Masculino", "Brasileiro(a)", "Casado(a)","Jurandir Afonso Oliveira Candido", "Maria Aparecida do Carmo Gomes de Oliveira");

-- EDITAR O ID DE UMA PESSOA ( VOU REALIZAR A TROCA DO ID DO SENHOR VALDECIR PARA 01 )
-- VOU DESATIVAR O MODO DE SEGURANÇA PARA REALIZAR A OPERAÇÃO

SET SQL_SAFE_UPDATES = 0;

-- VOU UTILIZAR O METODO FLOOR(RAND() * 1000) PARA MUDAR A PESSOA DE ID 01 PARA UM ALEATORIO DE 0 A 1000

UPDATE pessoas SET id = FLOOR(RAND() * 1000) WHERE id = 01;
UPDATE pessoas SET id = 1 WHERE nome LIKE "%Valdecir%";

-- VOU REATIVAR O MODO DE SEGURANÇA APÓS REALIZAR A OPERAÇÃoptimize

SET SQL_SAFE_UPDATES = 1;

SELECT * FROM pessoas;




				
                      