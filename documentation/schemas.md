# Tietokannan SQL-skeemat

Vertaa tarvittaessa [tietokantakaavioon](https://github.com/eetuahon/karatebase/blob/master/dbdiagram.png)

CREATE TABLE topics (
	id INTEGER NOT NULL, 
	"desc" TEXT, 
	PRIMARY KEY (id), 
	UNIQUE ("desc")
);

CREATE TABLE belts (
	id INTEGER NOT NULL, 
	belt TEXT, 
	PRIMARY KEY (id), 
	UNIQUE (belt)
);

CREATE TABLE senseis (
	id INTEGER NOT NULL, 
	name TEXT, 
	logon TEXT, 
	PRIMARY KEY (id), 
	UNIQUE (logon)
);

CREATE TABLE events (
	id INTEGER NOT NULL, 
    name TEXT, 
    day TEXT, 
    time TEXT, 
    info TEXT, 
    PRIMARY KEY (id), 
    UNIQUE (name)
);

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE beltevents (
	belt_id INTEGER NOT NULL, 
	event_id INTEGER NOT NULL, 
	PRIMARY KEY (belt_id, event_id), 
	FOREIGN KEY(belt_id) REFERENCES belts (id), 
	FOREIGN KEY(event_id) REFERENCES events (id)
);

CREATE TABLE topicevents (
	topic_id INTEGER NOT NULL, 
	event_id INTEGER NOT NULL, 
	PRIMARY KEY (topic_id, event_id), 
	FOREIGN KEY(topic_id) REFERENCES topics (id), 
	FOREIGN KEY(event_id) REFERENCES events (id)
);

CREATE TABLE senseievents (
	sensei_id INTEGER NOT NULL, 
	event_id INTEGER NOT NULL, 
	PRIMARY KEY (sensei_id, event_id), 
	FOREIGN KEY(sensei_id) REFERENCES senseis (id), 
	FOREIGN KEY(event_id) REFERENCES events (id)
);