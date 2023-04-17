Create database URBS

create table linhas(
	id int primary key not null,
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

select * from linhas;
select * from horario

insert into linhas values (231,'Banestado/california')