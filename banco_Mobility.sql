drop database mobility_volt;
create database mobility_volt;
\c mobility_volt

CREATE TABLE usuarios (
    codigo INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(120) NOT NULL,
    cpf	  BIGINT  NOT NULL UNIQUE,
    carteira Real NOT NULL
);

insert into usuarios values (1, 'Fibra Óptica', 'fibra@usp.br', '!@#$%234' , 123456789909, 34.45);
insert into usuarios values (2, 'Erikson', 'erikson@usp.br', '321234' , 234567899091, 124.45);
insert into usuarios values (3, 'Luiz', 'luiz@usp.br', '!@#$%asdf' , 345678990912, 12.00);
insert into usuarios values (4, 'Ivan', 'ivan@usp.br', '123456' , 456789909123, -12.67);
insert into usuarios values (5, 'Pedro', 'pedro@usp.br', '!@#$%asd' ,67856789909, 1.12);


CREATE TABLE regioes (
	codigo INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cidade VARCHAR (50) NOT NULL,
    localXi NUMERIC (9,6) NOT NULL,
	localYi NUMERIC (9,6) NOT NULL,
	localXs NUMERIC (9,6) NOT NULL,
	localYs NUMERIC (9,6) NOT NULL,
	constraint zona unique(nome,cidade)
);

insert into regioes values (1, 'USP-1', 'São Carlos', -22.004408,-47.895000,-22.07130, -47.900656);
insert into regioes values (2, 'centro', 'São Carlos', -22.021285,-47.890807,-22.026165, -47.891099); 
insert into regioes values (3, 'USP-2', 'São Carlos', -21.991901,-47.927256,-22.007162, -47.940536);


CREATE TABLE veiculos (
	codigo INT PRIMARY KEY,
	tipo INT NOT NULL,
	bateria INT  NOT NULL,
	localX NUMERIC (9,6) NOT NULL,
	localY NUMERIC  (9,6) NOT NULL,
	ped_regiao INT,
	FOREIGN KEY (ped_regiao) REFERENCES regioes(codigo)
);

insert into veiculos values (1,1,100,-22.004678,-47.897000,1);
insert into veiculos values (2,2,100,-22.004688,-47.897003,1);
insert into veiculos values (3,3,100,-22.004674,-47.897008,1);	

insert into veiculos values (4,1,100,-22.021295,-47.890897,2);
insert into veiculos values (5,2,100,-22.021295,-47.890900,2);
insert into veiculos values (6,3,100,-22.021695,-47.890897,2);	


insert into veiculos values (7,1,100,-21.991905,-47.927600,3);
insert into veiculos values (8,2,100,-21.991911,-47.927700,3);
insert into veiculos values (9,3,100,-21.991950,-47.937800,3);	


CREATE TABLE viagens (
	codigo INT PRIMARY KEY,
    distancia Real  NOT NULL,
    ped_usuario INT,
    ped_veiculo INT ,
    custo Real  NOT NULL,
    data date,
    hora time,
	FOREIGN KEY (ped_usuario) REFERENCES usuarios(codigo),
	FOREIGN KEY (ped_veiculo) REFERENCES veiculos(codigo)  
);
