DROP TABLE IF EXISTS "person" CASCADE;
DROP TABLE IF EXISTS "vehicle" CASCADE;
DROP TABLE IF EXISTS "state" CASCADE;
DROP TABLE IF EXISTS "city" CASCADE;
DROP TABLE IF EXISTS "section" CASCADE;
DROP TABLE IF EXISTS "crash" CASCADE;

CREATE TABLE "person"
( 
	"person_id" INTEGER NOT NULL,
    "person_kind" VARCHAR(255) NOT NULL,
    "person_state" VARCHAR(255) NOT NULL,
    "person_age" INTEGER NOT NULL,
	"person_sex" CHAR(1) NOT NULL,
    "crash_id" INTEGER NOT NULL, 
	PRIMARY KEY ("person_id"),
    FOREIGN KEY ("crash_id") REFERENCES "crash" 
);

CREATE TABLE "vehicle"
( 
	"vehicle_id" INTEGER NOT NULL,
    "vehicle_kind" VARCHAR(255)  NOT NULL,
    "vehicle_brand" VARCHAR(255)  NOT NULL,
	"vehicle_year" INTEGER  NOT NULL,
	"crashid" INTEGER  NOT NULL, 
	PRIMARY KEY ("vehicle_id"),
    FOREIGN KEY ("crash_id") REFERENCES "crash" 
);

CREATE TABLE "state"
( 
	"state_code" char(2) NOT NULL,
	"state_name" VARCHAR(255),
	PRIMARY KEY ("state_code"),
);

CREATE TABLE "city"
( 
	"city_code" INTEGER NOT NULL,
	"city_name" VARCHAR(255) NOT NULL,
	"state_code" char(2) NOT NULL,
	PRIMARY KEY ("city_name"),
	FOREIGN KEY ("state_code") REFERENCES "state" 
);

CREATE TABLE "section"
( 
	"section_code" INTEGER NOT NULL,
	"section_km" INTEGER NOT NULL,
	"section_date" DATE,
	"section_latitude" Decimal(8,6),
	"section_longitude" Decimal(8,6),
    "ic" NUMERIC,
    "ip" NUMERIC,
    "icm" NUMERIC,
	"city_name" INTEGER,
	PRIMARY KEY ("section_code", "section_km"),
	FOREIGN KEY ("city_name") REFERENCES "city" 
);

CREATE TABLE Crash
( 
	street_code INTEGER,
	beginning INTEGER,
	"end" INTEGER,
	vehicle_id INTEGER,
	person_id INTEGER,
	cause VARCHAR(255),
	classification VARCHAR(255),
	kind VARCHAR(255),
	weather VARCHAR(255),
	km INTEGER,
	track VARCHAR(255),
	"date" DATE,
	"hour" TIME,
	PRIMARY KEY (street_code, beginning, "end", vehicle_id, person_id),
	UNIQUE (street_code, beginning, "end", vehicle_id, person_id),
	FOREIGN KEY (person_id) REFERENCES Person,
	FOREIGN KEY (vehicle_id) REFERENCES Vehicle, 
	FOREIGN KEY (street_code, beginning, "end") REFERENCES HighwaySection 
);