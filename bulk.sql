select id_client from client where id_client > 7;
select id_home from home where id_home>=4000000;
select * from client where id_client = 1001626;

   
select count(*) from device;


-- psql -U postgres -d SchecDB -h localhost
\copy client (id_client, name, email, password)
FROM 'C:/Users/yosti/OneDrive/Desktop/2 millones/prueba.csv'
WITH (FORMAT csv, HEADER true
