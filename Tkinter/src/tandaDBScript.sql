BEGIN TRANSACTION;
CREATE TABLE "Tandas" (
	`idTandas`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`noIntegrantes`	INTEGER NOT NULL,
	`fechaInicio`	REAL NOT NULL,
	`idPer`	INTEGER NOT NULL,
	`monto`	REAL,
	`finalizada`	INTEGER
);
CREATE TABLE "TandaSalida" (
	`idTandas`	INTEGER NOT NULL,
	`idIntegrante`	INTEGER NOT NULL,
	`pagado`	INTEGER,
	PRIMARY KEY(idTandas,idIntegrante)
);
CREATE TABLE "TandaEntrada" (
	`idTandas`	INTEGER NOT NULL,
	`idIntegrante`	INTEGER NOT NULL,
	`pos`	INTEGER NOT NULL,
	`pagado`	INTEGER,
	PRIMARY KEY(idTandas,idIntegrante,pos)
);
CREATE TABLE "Periodicidad" (
	`idPer`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`tipoPeriodo`	TEXT NOT NULL
);
CREATE TABLE "Integrantes" (
	`idIntegrante`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`nombre`	TEXT NOT NULL,
	`apellido`	TEXT,
	`telefono`	TEXT
);
COMMIT;
