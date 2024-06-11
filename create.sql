DROP TABLE IF EXISTS "bd1_accidents_person";
DROP TABLE IF EXISTS "bd1_accidents_vehicle";
DROP TABLE IF EXISTS "bd1_accidents_state";
DROP TABLE IF EXISTS "bd1_accidents_city";
DROP TABLE IF EXISTS "bd1_accidents_section";
DROP TABLE IF EXISTS "bd1_accidents_crash";

CREATE TABLE "bd1_accidents_state"
(
   "state_code" char(2) NOT NULL,
   "state_name" VARCHAR(255) NOT NULL,
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
   "section_date" DATE NOT NULL,
   "section_latitude" DOUBLE PRECISION NOT NULL,
   "section_longitude" DOUBLE PRECISION NOT NULL,
   "section_ic" NUMERIC NOT NULL,
   "section_ip" NUMERIC NOT NULL,
   "section_icm" NUMERIC NOT NULL,
   "section_panela" CHAR(1) NOT NULL,
   "section_remendo" CHAR(1) NOT NULL,
   "section_trincamento" CHAR(1) NOT NULL,
   "section_rocada" CHAR(1) NOT NULL,
   "section_drenagem" CHAR(1) NOT NULL,
   "section_sinalizacao" CHAR(1) NOT NULL,
   "city_name" VARCHAR(255) NOT NULL,
   PRIMARY KEY ("section_br", "section_km"),
   FOREIGN KEY ("city_name") REFERENCES "bd1_accidents_city"
);

CREATE TABLE "bd1_accidents_crash"
(
   "crash_id" INTEGER NOT NULL,
   "crash_date" DATE NOT NULL,
   "crash_time" TIME NOT NULL,
   "section_br" INTEGER NOT NULL,
   "section_km" INTEGER NOT NULL,
   "crash_cause" VARCHAR(255) NOT NULL,
   "crash_kind" VARCHAR(255) NOT NULL,
   "crash_classification" VARCHAR(255) NOT NULL,
   "crash_day_phase" VARCHAR(255) NOT NULL,
   "crash_track_direction" VARCHAR(255) NOT NULL,
   "crash_weather" VARCHAR(255) NOT NULL,
   "crash_track_kind" VARCHAR(255) NOT NULL,
   "crash_track_layout" VARCHAR(255) NOT NULL,
   "crash_ground" CHAR(3) NOT NULL,
   "crash_uninjured" INTEGER NOT NULL,
   "crash_slightly_injured" INTEGER NOT NULL,
   "crash_seriously_injured" INTEGER NOT NULL,
   "crash_deaths" INTEGER NOT NULL,
   "crash_latitude" DOUBLE PRECISION NOT NULL,
   "crash_longitude" DOUBLE PRECISION NOT NULL,
   "crash_delegacy" VARCHAR(255) NOT NULL,
   "crash_uop" VARCHAR(255) NOT NULL,
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