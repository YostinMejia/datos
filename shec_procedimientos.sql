/* 
 	Procedimientos
	 
1) logear en la tabla binnacle cuando el usuario inicia sesión

2) verificar que los datos al crear un device sean validos:
	name != " ",
	time_on > 0,
	expent > 0

3) validar que el correo tenga el formato correcto

	Vistas

1)
*/

-- 1) logear en la tabla binnacle cuando el usuario inicia sesión

create or replace procedure log_user_login(p_id_client int) language plpgsql
as $$
begin

	INSERT INTO client_binnacle(timestamp, operation, name_table, id_client) VALUES 
	(current_timestamp, 'LOGIN', 'client', p_id_client);
	
	commit;
	
end;
$$
call log_user_login(3);

select * from client_binnacle;

/*

2) verificar que los datos al crear un device sean validos:
	name != " ",
	time_on > 0,
	expent > 0

	y lo crea
*/

create or replace procedure handle_insert_device(p_id_home int,p_name varchar(255), p_time_on int, p_expent int) language plpgsql
as $$
begin

	if trim(p_name) ='' then
		raise exception 'El atributo "name" no puede ser una cadena vacía';
	end if;
	if (p_time_on <0) or (p_expent <0) then
		raise exception 'los atributos "time_on" y "expent" no pueden ser negativos';
	end if;

	insert into device (id_home,name,time_on,expent) values (p_id_home ,p_name , p_time_on , p_expent );
	
	commit;
	
end;
$$

select * from device;
call handle_insert_device(1,'  ',1,56);
select * from home;

/* VISTAS */


-- 1) view_bill

create view view_bill as
select 
h.id_home,
b.emition_date,
b.price_kw,
	h.stratum,
   sum(d.time_on) as total_time_on,
   (sum (d.time_on)* b.price_kw) as total_cost
   
from 
    home h
join 
    device d ON h.id_home = d.id_home 
join 
	bill b on b.id_home = h.id_home
group by
	 h.id_home, b.emition_date, b.price_kw
	
select * from view_bill;