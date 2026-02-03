use role accountadmin;
use warehouse my_warehouse;
use schema my_db.my_schema;
show procedures;
select * from information_schema.procedures;
execute immediate
$$
begin
    return 'Hello, Snowflake!';
end;
$$;
create or replace procedure pr_hello()
returns string
language sql
execute as caller
as
$$
begin
    return 'Hello, Snowflake!';
end;
$$;
call pr_hello();
create or replace procedure pr_add_numbers(a int, b int)
returns int
language sql
execute as caller
as
$$
begin
    return a + b;
end;
$$; 
call pr_add_numbers(5, 10);
execute immediate 
$$
declare
    first_name varchar default 'siva';
    last_name varchar default 'reddy';
    full_name varchar;
begin
    let middle_name := 'vardhana';
    full_name := first_name || ' ' || middle_name || ' ' || last_name;
    --select :first_name || ' ' || :middle_name || ' ' || :last_name into :full_name from dual;
    return full_name;
end;
$$;
set age = 34;
select $age from dual;
execute immediate
$$
declare 
    out_str varchar := '';
begin
    for i in 1 to 20 
    loop
        out_str := out_str || ' ' || i;
    end loop;
    return out_str;
end;
$$;
execute immediate
$$
declare
    out_str varchar := '';
    cnt int := 1;
begin
    while (cnt <=20)
    loop
        out_str := out_str || ' ' || cnt;
        cnt := cnt + 1;
    end loop;
    return trim(out_str);
end;
$$;
execute immediate
$$
declare
    c1 cursor for select * from emp;
    v_total_sal number:=0; 
begin
    for i in c1
    loop
        v_total_sal := v_total_sal + i.SAL;
    end loop;
    return v_total_sal;
end;
$$;
create or replace procedure pr_cursor_prac_1(p_table_name varchar)
returns number
language sql
execute as caller
as
$$
declare
    c1 cursor for select * from identifier(?);
    v_total_sal number:=0;
begin
    open c1 using(p_table_name);
    for i in c1
    loop
        v_total_sal := v_total_sal + i.SAL;
    end loop;
    close c1;
    return v_total_sal;
end;
$$;
call pr_cursor_prac_1('EMP');
execute immediate
$$
declare
    c1 cursor for select * from identifier(?) where identifier(?) = ?;
    v_total_sal number:=0;
    v_deptno int := 30;
    v_table_name varchar := 'EMP';
    v_column_name varchar := 'DEPTNO';
begin
    open c1 using(v_table_name, v_column_name, v_deptno);
    for i in c1
    loop
        v_total_sal := v_total_sal + i.SAL;
    end loop;
    close c1; 
    return v_total_sal;
end;
$$;
execute immediate
$$
declare
    v_sql varchar := '';
    v_res resultset;
    v_n number:=1;
    v_deptno number:=30;
begin
    v_sql := 'select * from emp where sal in (
                select sal from (
                select sal,dense_rank() over(order by sal desc) dn from emp where deptno=' || :v_deptno || ')
                where dn<=' || :v_n || ')';
    v_res := (execute immediate v_sql); 
    return table(v_res);
end;
$$;
execute immediate
$$
declare
    c1 cursor for select * from emp where deptno = ?;
    v_deptno number :=40;
    v_cnt number := 0;
begin
    select count(*) into :v_cnt from emp where deptno = :v_deptno;
    if (v_cnt = 0) then
        return 'No records found for deptno ' || :v_deptno;
    end if;
    open c1 using(:v_deptno);
    return table(resultset_from_cursor(c1));
    close c1;
end;
$$;