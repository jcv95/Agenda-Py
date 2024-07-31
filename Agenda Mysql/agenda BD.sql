create database if not exists agenda;
use agenda;
create table contactos (registro int auto_increment primary key, nombre varchar(25), apellido varchar(25), telefono varchar(15), direccion varchar(50);
insert into contactos (nombre, apellido, telefono, direccion ) values ('Armando', 'Rodriguez', '1537135487','Viamonte 111');
insert into contactos (nombre, apellido, telefono, direccion ) values ('Nahuel', 'Illinois', '1563013408','Pichincha 222');
insert into contactos (nombre, apellido, telefono, direccion ) values ('Paz', 'Diegoli', '1575469312','Riobamba 333');
select * from contactos;