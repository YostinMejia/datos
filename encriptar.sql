select * from client;
select crypt('password',gen_salt('md5'));

/*Crea un trigger para encriptar*/
CREATE OR REPLACE FUNCTION encrypt_password_trigger()
RETURNS TRIGGER AS $$
BEGIN
    NEW.password = crypt(NEW.password, gen_salt('md5'));
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER encrypt_password
BEFORE INSERT ON client
FOR EACH ROW
EXECUTE FUNCTION encrypt_password_trigger();

/*Mirar si es igual*/

create or replace function is_valid_pwd(pwd varchar, pwd_hash text) returns bool
LANGUAGE plpgsql
as $$

begin
	return crypt(pwd, pwd_hash) = pwd_hash;
end;
$$

select encrypt_pwd('hola');
select is_valid_pwd('hola','$1$24Kw9wmF$rrLBQTRzl6C05eNxXVmKb1');

