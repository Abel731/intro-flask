create table 
	ciudades(
		id serial primary KEY
		, descripcion varchar(60) UNIQUE
	);
	
	SELECT id, descripcion 
        FROM ciudades;
 
CREATE TABLE paises (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) UNIQUE
);

-- (Opcional) Consulta para ver el contenido de la tabla paises
SELECT id, descripcion 
FROM paises;