DROP TABLE IF EXISTS "bd1_accidents_person";
DROP TABLE IF EXISTS "bd1_accidents_vehicle";
DROP TABLE IF EXISTS "bd1_accidents_state";
DROP TABLE IF EXISTS "bd1_accidents_city";
DROP TABLE IF EXISTS "bd1_accidents_section";
DROP TABLE IF EXISTS "bd1_accidents_crash";

CREATE TABLE "bd1_accidents_state"
( 
	"state_code" char(2) NOT NULL,
	"state_name" VARCHAR(255),
	PRIMARY KEY ("state_code")
);

CREATE TABLE "bd1_accidents_city"
( 
	"city_code" INTEGER NOT NULL,
	"city_name" VARCHAR(255) NOT NULL,
	"state_code" char(2) NOT NULL,
	PRIMARY KEY ("city_name"),
	FOREIGN KEY ("state_code") REFERENCES "bd1_accidents_state" 
);

CREATE TABLE "bd1_accidents_section"
( 
	"section_br" INTEGER NOT NULL,
	"section_km" INTEGER NOT NULL,
	"section_date" DATE,
	"section_latitude" DOUBLE PRECISION,
	"section_longitude" DOUBLE PRECISION,
    "section_ic" NUMERIC,
    "section_ip" NUMERIC,
    "section_icm" NUMERIC,
	"city_name" VARCHAR(255),
	PRIMARY KEY ("section_br", "section_km"),
	FOREIGN KEY ("city_name") REFERENCES "bd1_accidents_city" 
);

CREATE TABLE "bd1_accidents_crash"
( 
	"crash_id" INTEGER NOT NULL,
	"crash_date" DATE,
	"crash_time" TIME,
	"section_br" INTEGER,
	"section_km" INTEGER,
    "crash_cause" VARCHAR(255),
    "crash_kind" VARCHAR(255),
	"crash_classification" VARCHAR(255),
	"crash_day_phase" VARCHAR(255),
	"crash_track_direction" VARCHAR(255),
	"crash_weather" VARCHAR(255),
	"crash_track_kind" VARCHAR(255),
	"crash_track_layout" VARCHAR(255),
	"crash_ground" CHAR(3),
	"crash_uninjured" INTEGER,
	"crash_slightly_injured" INTEGER,
	"crash_seriously_injured" INTEGER,
	"crash_deaths" INTEGER,
	"crash_latitude" DOUBLE PRECISION,
	"crash_longitude" DOUBLE PRECISION,
	"crash_delegacy" VARCHAR(255),
	"crash_uop" VARCHAR(255),
	PRIMARY KEY ("crash_id"),
	FOREIGN KEY ("section_br", "section_km") REFERENCES "bd1_accidents_section" 
);

CREATE TABLE "bd1_accidents_person"
( 
	"person_id" INTEGER NOT NULL,
    "person_kind" VARCHAR(255) NOT NULL,
    "person_state" VARCHAR(255) NOT NULL,
    "person_age" INTEGER NOT NULL,
	"person_sex" CHAR(1) NOT NULL,
    "crash_id" INTEGER NOT NULL, 
	PRIMARY KEY ("person_id"),
    FOREIGN KEY ("crash_id") REFERENCES "bd1_accidents_crash" 
);

CREATE TABLE "bd1_accidents_vehicle"
( 
	"vehicle_id" INTEGER NOT NULL,
    "vehicle_kind" VARCHAR(255)  NOT NULL,
    "vehicle_brand" VARCHAR(255)  NOT NULL,
	"vehicle_year" INTEGER  NOT NULL,
	"crash_id" INTEGER  NOT NULL, 
	PRIMARY KEY ("vehicle_id"),
    FOREIGN KEY ("crash_id") REFERENCES "bd1_accidents_crash" 
);