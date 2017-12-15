Title: pg_protobuf: Protobuf support for PostgreSQL
Category: PostgreSQL
Date: 2017-12-15 13:00
Modified: 2017-12-15 13:00
Slug: pg-protobuf

Yesterday I had a few spare hours (I was waiting for 'Star Wars VIII' movie
session, which BTW turned out to be great) so I decided to implement one idea I
had in mind for quite some time. The idea is to add support of Protobuf datatype
to PostgreSQL.

The result can be [found on GitHub][gh]. Here is a short example from README.md:

```
create extension pg_protobuf;

create table heroes (x bytea);

insert into heroes values
  (E'\\x0a0365617810321880022202100f'),
  (E'\\x0a07616669736b6f6e10191880082a060a0200011064')
  -- ...
  ;

create function hero_name(x bytea) returns text as $$
begin
return protobuf_get_string(x, 1);
end
$$ language 'plpgsql' immutable;

create function hero_hp(x bytea) returns text as $$
begin
return protobuf_get_integer(x, 2);
end
$$ language 'plpgsql' immutable;

create function hero_xp(x bytea) returns text as $$
begin
return protobuf_get_integer(x, 3);
end
$$ language 'plpgsql' immutable;

create index hero_name_idx on heroes using btree(hero_name(x));

select protobuf_decode(x) from heroes where hero_name(x) = 'afiskon';
```

The extension seems to work and pass basic tests, however more thorough testing
is required which I'm going to do in nearest few days.

Basically pg\_protobuf solves same issues that [zson][zson] solves but without
any shared dictionaries that should be relearned from time to time.

[gh]: https://github.com/afiskon/pg_protobuf
[zson]: https://github.com/postgrespro/zson
