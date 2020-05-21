-- esquema.sql
-- Toda definição de banco deverá ser feita nesse arquivo

drop table if exists mensagens;
create table mensagens (
  id integer primary key autoincrement,
  usuario string not null,
  texto string not null
);


drop table if exists presenca;
create table presenca (
  id integer primary key autoincrement,
  email string not null,
  presenca bit not null,
  resposta string,
  comentario string

);
