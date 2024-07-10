create database python_bd;

use python_bd;

create table usuarios(
	id int primary key auto_increment,
    destino varchar(50),
    excursion varchar(50),
    precio float(10,2)
);

insert into usuarios(id, destino, excursion, precio) 
values(1,'Cataratas','Caminata','15000');

select * from usuarios;
