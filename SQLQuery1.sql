Create database URBS

create table linhas(
	id int primary key identity(1,1) not null,
	identificacao varchar(5),
	nome varchar(100) not null
);

create table horario(
	id int primary key identity(1,1) not null,
	ponto varchar(50) not null,
	tipo_dia varchar(10) not null,
	horario varchar(5) not null,
	id_linha int not null foreign key references linhas(id)
);
-- drop table horario
-- drop table linhas

-- ------------------------ testes ---------------------------

select horario.horario, horario.tipo_dia, horario.ponto from horario join linhas on horario.id_linha = linhas.id 
where linhas.identificacao = '231'

select * from linhas
select count(*) from horario

select * from linhas;
select * from horario
select * from linhas where identificacao = '231'
select * from linhas where nome like '%BOQUEIR�O%'
insert into linhas values ('X03','Banestado/california')
-- ------------------------ testes ---------------------------