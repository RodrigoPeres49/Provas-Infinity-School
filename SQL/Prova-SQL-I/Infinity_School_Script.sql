CREATE DATABASE IF NOT EXISTS Infinity_School;

USE Infinity_School;

CREATE TABLE curso (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(100) NOT NULL
);

CREATE TABLE aluno (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT 1,
    matricula VARCHAR(5) NOT NULL UNIQUE,
    curso_id INTEGER NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES curso (id)
);


CREATE TABLE materia (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(100) NOT NULL,
    sigla VARCHAR(3) NOT NULL
);

CREATE TABLE materia_curso(
	materia_id INTEGER NOT NULL,
    curso_id INTEGER NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES curso (id),
    FOREIGN KEY (materia_id) REFERENCES materia(id)
);

CREATE TABLE professor (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    ativo BOOLEAN NOT NULL DEFAULT 1,
    materia_id INTEGER NOT NULL,
    FOREIGN KEY (materia_id) REFERENCES materia (id)
);

CREATE TABLE turma (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    sala VARCHAR(50) NOT NULL,
    professor_id INTEGER NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    dia_semana VARCHAR(15) NOT NULL,
    hora_aula TIME NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES professor (id)
);

CREATE TABLE aluno_turma ( 
    aluno_id INTEGER NOT NULL, 
	turma_id INTEGER NOT NULL,
	FOREIGN KEY (aluno_id) REFERENCES aluno (id),
	FOREIGN KEY (turma_id) REFERENCES turma (id));