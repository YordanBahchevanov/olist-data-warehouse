/*
==========================================================
Create Schemas
==========================================================

Script Purpose:
    Creates the schemas used in the Data Warehouse project.

Schemas:
    - bronze: Raw imported data
    - silver: Cleaned and transformed data
    - gold: Business-ready analytical tables


==========================================================
*/

CREATE SCHEMA IF NOT EXISTS bronze;

CREATE SCHEMA IF NOT EXISTS silver;

CREATE SCHEMA IF NOT EXISTS gold;