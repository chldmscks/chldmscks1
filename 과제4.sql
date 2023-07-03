CREATE TABLE Test
(
  ID INT NOT NULL,
  NAME VARCHAR(30),
  ReserveData DATE,
  RoomNum INT,
  PRIMARY KEY(id)
);

CREATE TABLE chl
(
	datentime VARCHAR(31) NOT NULL,
	pty INT,
	reh INT,
	rn1 INT,
	t1h FLOAT,
	uuu FLOAT,
	vec INT,
	vvv FLOAT,
	wsd FLOAT,
	PRIMARY KEY(datentime)
);

#DROP TABLE chl
DESC chl1
SELECT * FROM chl