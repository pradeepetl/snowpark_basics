use role accountadmin;
use warehouse my_warehouse;
use schema my_db.my_schema;
show integrations;
desc integration AWS_INT;
drop schema if exists my_db.control;
drop schema if exists my_db.stagging;
drop stage if exists my_db.control.int_stage;
create table if exists my_db.control.tbl_copy_data;
create schema if not exists my_db.control;
create schema if not exists my_db.stagging;
use schema my_db.control;
create table if not exists my_db.control.tbl_copy_data
(
    database_name       string,
    schema_name         string,
    stage_table_name    string,
    storage_int         string,
    storage_loc         string,
    files_type          string,
    file_pattren        string,
    file_format         string,
    file_delimiter      string,
    on_error            string,
    skip_header         number,
    force               boolean,
    trunacte_cols       boolean,
    is_active           boolean
);
use schema my_db.stagging;
CREATE OR REPLACE TABLE my_db.stagging.customer_data 
(
customerid NUMBER,
custname STRING,
email STRING,
city STRING,
state STRING,
DOB DATE
);

CREATE OR REPLACE TABLE my_db.stagging.pets_data_raw 
(raw_file variant);

CREATE OR REPLACE TABLE my_db.stagging.emp_data 
(
  id INT,
  first_name STRING,
  last_name STRING,
  email STRING,
  location STRING,
  department STRING
);

CREATE OR REPLACE TABLE my_db.stagging.customer
(
customerid NUMBER,
custname STRING,
email STRING,
city STRING,
state STRING,
DOB DATE
);

create or replace procedure my_db.stagging.proc_data_load()
returns varchar
language sql
execute as caller
as
$$
declare 
    v_ld_cur cursor for (select * from my_db.control.tbl_copy_data where is_active = True);
    v_database_name       string;
    v_schema_name         string;
    v_stage_table_name    string;
    v_storage_int         string;
    v_storage_loc         string;
    v_files_type          string;
    v_file_pattren        string;
    v_file_format         string;
    v_file_delimiter      string;
    v_on_error            string;
    v_skip_header         number;
    v_force               boolean;
    v_trunacte_cols       boolean;
    v_file_format_stmt    string;
    v_copy_stmt           string; 
    v_return              string;
begin
    v_return :='';
    for rw in v_ld_cur
    loop
        v_database_name := rw.database_name;    
        v_schema_name := rw.schema_name;
        v_stage_table_name := rw.stage_table_name;
        v_storage_int := rw.storage_int;
        v_storage_loc := rw.storage_loc;
        v_files_type := rw.files_type;
        v_file_pattren := rw.file_pattren;
        v_file_format := rw.file_format;
        v_file_delimiter := rw.file_delimiter;
        v_on_error := rw.on_error;
        v_skip_header := rw.skip_header;
        v_force := rw.force;
        v_trunacte_cols := rw.trunacte_cols;    
    if (:v_file_format is null) 
    then
        v_file_format_stmt := v_file_format;
    end if;
    end loop;
end;
$$;