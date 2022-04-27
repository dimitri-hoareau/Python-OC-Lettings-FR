PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "profiles_profile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "favorite_city" varchar(64) NOT NULL, "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO profiles_profile VALUES(1,'Buenos Aires',5);
INSERT INTO profiles_profile VALUES(2,'Barcelona',4);
INSERT INTO profiles_profile VALUES(3,'Budapest',3);
INSERT INTO profiles_profile VALUES(4,'Berlin',2);
COMMIT;
