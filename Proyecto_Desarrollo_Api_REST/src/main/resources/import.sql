
insert into categoria (id, nombre) values (NEXTVAL('hibernate_sequence'), 'Bebidas')
insert into categoria (id, nombre) values (NEXTVAL('hibernate_sequence'), 'Comida')
insert into categoria (id, nombre) values (NEXTVAL('hibernate_sequence'), 'Ropa')

insert into producto (id, nombre, precio, categoria_id) values(NEXTVAL('hibernate_sequence'), 'Coca-cola', 1.20, 1)
insert into producto (id, nombre, precio, categoria_id) values(NEXTVAL('hibernate_sequence'), 'Camiseta', 15, 3)
insert into producto (id, nombre, precio, categoria_id) values(NEXTVAL('hibernate_sequence'), 'Doritos', 1.35, 2)
insert into producto (id, nombre, precio, categoria_id) values(NEXTVAL('hibernate_sequence'), 'Pantalones vaqueros', 30, 3)
insert into producto (id, nombre, precio, categoria_id) values(NEXTVAL('hibernate_sequence'), 'Cerveza', 1.0, 1)
