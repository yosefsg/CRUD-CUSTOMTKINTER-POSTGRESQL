-- Añadiendo cosas al inventario

INSERT INTO INVENTARIO (descripcion, cantidad)
VALUES
	('Tornillos 1/8', 80),
	('Multímetro', 4),
	('Compresores', 4),
	('Soldadores', 4),
	('Aceites', 50),
	('Termostatos', 50),
	('Aislantes termicos', 50);
	
-- Añadiendo trabajadores
INSERT INTO TRABAJADOR (nombre, apellidop, apellidom, telefono)
VALUES
	('Alvaro', 'Casillas', 'Estrada', '3345896572'),
	('Pablo', 'Avelar', 'Armenta', '3356895420'),
	('Yosef', 'Sánchez', 'Gutiérrez', '3356897745');

INSERT INTO CLIENTE(nombre, apellidop, apellidom, calle, colonia, codigopostal, numext, numint, telefono, correo)
VALUES 
('Ana', 'García', 'López', 'Calle 1', 'Centro', '12345', '100', 'A', '1234567890', 'ana@example.com'),
('Juan', 'Martínez', 'Hernández', 'Calle 2', 'Reforma', '23456', '200', 'B', '0987654321', 'juan@example.com'),
('María', 'Rodríguez', 'Pérez', 'Calle 3', 'Las Rosas', '34567', '300', 'C', '55551234', 'maria@example.com'),
('Pedro', 'López', 'Gómez', 'Calle 4', 'San Rafael', '45678', '400', 'D', '77778888', 'pedro@example.com'),
('Laura', 'Díaz', 'Fernández', 'Calle 5', 'La Loma', '56789', '500', 'E', '99990000', 'laura@example.com'),
('Carlos', 'González', 'Sánchez', 'Calle 6', 'Del Valle', '67890', '600', 'F', '33334444', 'carlos@example.com'),
('Sofía', 'Hernández', 'Gutiérrez', 'Calle 7', 'Las Águilas', '78901', '700', 'G', '22223333', 'sofia@example.com'),
('Javier', 'Pérez', 'Martínez', 'Calle 8', 'Los Pinos', '89012', '800', 'H', '44445555', 'javier@example.com'),
('Elena', 'Sánchez', 'Luna', 'Calle 9', 'Bosques', '90123', '900', 'I', '66667777', 'elena@example.com'),
('Diego', 'Ramírez', 'Torres', 'Calle 10', 'Lomas Altas', '01234', '1000', 'J', '11112222', 'diego@example.com');

-- Añadiendo citas
INSERT INTO CITA (idCliente, fecha, cotizacion, descripcion, lugar)
VALUES
    (1, '2023-12-10', 150, 'Reparación de compresor', 'Local del cliente'),
    (2, '2023-11-28', 200, 'Mantenimiento de sistema de enfriamiento', 'Taller de la empresa'),
    (3, '2023-12-05', 100, 'Reemplazo de válvula de expansión', 'Domicilio del cliente'),
    (4, '2023-12-15', 300, 'Instalación de nuevo condensador', 'Oficina principal'),
    (5, '2023-11-30', 180, 'Limpieza y mantenimiento general', 'Sitio designado por el cliente');

-- Añadiendo equipos de clientes
INSERT INTO EQUIPO (idcliente, hp_compresor, voltaje, marca, capacidad, descripcion, hp_ventiladores)
VALUES
    (1, 2.5, '220V', 'Samsung', '5000 BTU', 'Aire acondicionado de ventana', 0.5),
    (2, 3.0, '110V', 'LG', '12000 BTU', 'Split de pared', 0.8),
    (3, 4.0, '220V', 'Carrier', '18000 BTU', 'Unidad central', 1.2),
    (4, 2.0, '220V', 'Whirlpool', '8000 BTU', 'Aire portátil', 0.6),
    (5, 5.0, '110V', 'Haier', '24000 BTU', 'Split de techo', 1.5);

/*
INSERT INTO HISTORIAL (idcliente, fecha, costo, descripcion)
VALUES
    (1, '2023-10-15', 200, 'Reparación de compresor y limpieza general'),
    (2, '2023-09-28', 150, 'Mantenimiento preventivo del sistema de enfriamiento'),
    (3, '2023-11-05', 300, 'Reemplazo de válvula de expansión y carga de refrigerante'),
    (4, '2023-10-20', 180, 'Instalación de nuevo condensador y ajustes de temperatura'),
    (5, '2023-11-10', 250, 'Reparación de motor de ventilador y revisión completa del equipo');
*/

/*
INSERT INTO FACTURA (idfactura, idhistorial, idcliente, fecha, costo, rfc, descripcion, metodo_pago)
VALUES
    (1, 1, 1, '2023-10-20', 220, 'ABC123456XYZ', 'Servicio de reparación y mantenimiento', 'Tarjeta de crédito'),
    (2, 2, 2, '2023-09-30', 180, 'DEF789012ABC', 'Mantenimiento preventivo', 'Transferencia bancaria'),
    (3, 3, 3, '2023-11-10', 320, 'GHI345678BCD', 'Reemplazo de componentes y servicio de carga', 'Efectivo'),
    (4, 4, 4, '2023-10-25', 200, 'JKL901234CDE', 'Instalación de nuevo condensador', 'Cheque'),
    (5, 5, 5, '2023-11-15', 270, 'MNO567890DEF', 'Reparación de motor y mantenimiento general', 'Transferencia bancaria');
*/
INSERT INTO CREDITO (idcredito, idcliente, fecha, limitepago, totalapagar)
VALUES
    (1, 1, '2023-12-01', '2024-01-01', 2000),
    (2, 2, '2023-11-20', '2023-12-20', 1800),
    (3, 3, '2023-12-05', '2024-01-05', 5400),
    (4, 4, '2023-11-25', '2023-12-25', 1080),
    (5, 5, '2023-12-10', '2024-01-10', 975);
	
INSERT INTO ABONOS (idabonos, idcredito, monto)
VALUES
    (1, 1, 100),
    (2, 2, 80),
    (3, 3, 120),
    (4, 4, 90),
    (5, 5, 150);
