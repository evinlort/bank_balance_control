\connect bbc;
CREATE SCHEMA IF NOT EXISTS migrations;
CREATE TABLE IF NOT EXISTS migrations.plan (
    migration text,
    apply_order INTEGER
);
CREATE TABLE IF NOT EXISTS migrations.migrated (migration text);