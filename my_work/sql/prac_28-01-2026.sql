use role accountadmin;
use warehouse my_warehouse;
use schema my_db.my_schema;
execute immediate
$$
declare
    v_cnt int:=0;
    v_sql varchar:='';
    no_data_found exception(-20001,'No data found in department');
    v_deptno int :=40;
begin
    select count(*) into v_cnt from emp where deptno=:v_deptno;
    if (v_cnt = 0) then
        raise no_data_found;
    end if;
    return 'Total employees in deptno ' || :v_deptno || ': ' || v_cnt;
exception
    when statement_error then
        return object_construct('error type','statement_error','message',sqlerrm,'sqlcode',sqlcode,
        'error state',sqlstate,'error_date',current_timestamp());
    when expression_error then
        return object_construct('error type','expression_error','message',sqlerrm,'sqlcode',sqlcode,
        'error state',sqlstate,'error_date',current_timestamp());
    when no_data_found then
        return object_construct('error type','no_data_found','message',sqlerrm,'sqlcode',sqlcode,
        'error state',sqlstate,'error_date',current_timestamp());
    when other then
        return object_construct('error type','others','message',sqlerrm,'sqlcode',sqlcode,
        'error state',sqlstate,'error_date',current_timestamp());
end;
$$;
select * from information_schema.tables;
select * from table(information_schema.copy_history
(table_name => 'HOTEL_BOOKINGS',start_time=>dateadd(hours,-10000,current_timestamp())))