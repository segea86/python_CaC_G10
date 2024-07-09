create database python_bd;

use python_bd;

create table usuarios(
	id int primary key auto_increment,
    destino varchar(20),
    excursion varchar(20),
    precio varchar(20)
);

insert into usuarios(id, destino, excursion, precio) 
values(1,'Cataratas','Caminata','15000');

select * from usuarios;
