Title: PostgreSQL GSoC 2018 ideas
Category: PostgreSQL
Date: 2017-12-15 14:30
Modified: 2017-12-15 15:16
Slug: gsoc2018-ideas

Recently Stephen Frost [called][hackers] in pgsql-hackers@ mailing list for
PostgreSQL-related ideas for Google Summer of Code 2018. I&nbsp;proposed a few ideas
and offered to be a possible mentor for corresponding projects. In this post I
would like to share a brief description of these projects (copied from [PostgreSQL
Wiki][wiki]).

[Google Summer of Code][gsoc] is a great opportunity to contribute to free and open
source software, not mentioning gaining unique experience. If you are a student
you should seriously consider to participate. Also I would like to encourage
everyone to join the discussion in the mailing list and propose ideas on how
PostgreSQL can be improved.

## Project 1. High availability / failover based on logical replication

Currently there are plenty HA solutions for PostgreSQL based on physical
(streaming) replication - patroni, Stolon, RepMgr, and others. Unfortunately,
there is no solution that uses logical replication introduced in PostgreSQL 10.
The main advantage of logical replication over physical replication in this
context is an ability to upgrade PostgreSQL without a downtime. Also logical
replication allows to use temporary tables on replicas. The idea of this project
is to implement an analogue of Stolon that will provide HA based on logical
replication.

It worth noticing that this tool has a potential to evolve in a full-feature
open source NewSQL layer on top of PostgreSQL that will support sharding,
rebalancing (which is also impossible with physical replication),
Percolator-like distributed transactions, convenient web-panel, etc. These are
subjects for further GSoC projects though.

## Project 2. Thrift datatype support

One of the advantages of document-oriented databases like MongoDB or Couchbase
over RDBMSs is an ability to change the data scheme easily, fast and often. The
traditional approach in RDBMS world involves doing an expensive ALTER TABLE
operation, slow upgrade of an existing data, and stuff like this. This approach
is often slow and inconvenient for application developers.

To solve this issue PostgreSQL provides JSON and JSONB datatypes. Unfortunately
JSONB has a disadvantage of storing all documents keys, which is a lot of
redundant data.

One possibility to reduce JSONB redundancy is to use [zson][zson] extension.  It
compresses JSONB documents using a shared dictionary of common strings that
appear in all or most documents. This approach has its limitations though.
Particularly, since data schema evolves, the dictionary has to be updated from
time to time. Also zson can affect the build-in mechanism of PostgreSQL of
compressing data using PGLZ algorithm since this mechanism uses some heuristics
to recognize data that compresses well. Thus sometimes zson can reduce the
overall performance.

There is another extension - [pg\_protobuf][pgpb]. Basically, it provides
Protobuf support for PostgreSQL. At the time of writing this text pg\_protobuf
is in a proof-of-concept state. However, it seems to solve all the issues
described above and doesn't have any disadvantages of zson extension.

The idea of this project is to create a similar extension that would provide
Thrift support. Some users may prefer Thrift to Protobuf or just use it for
historical reasons. This project is a bit more complicated than pg\_protobuf
since unlike Protobuf Thrift supports various encoding protocols. Also the
extension should provide a tool that generates from .thrift files PL/pgSQL
procedures to access Thrift data (at the time of writing this text similar tool
for pg\_protobuf is in development.)

[wiki]: https://wiki.postgresql.org/wiki/GSoC_2018
[hackers]: https://postgr.es/m/20171215031424.GE4628%40tamriel.snowman.net
[zson]: https://afiskon.github.io/zson-v1-1.html
[pgpb]: https://afiskon.github.io/pg-protobuf.html
[gsoc]: https://en.wikipedia.org/wiki/Google_Summer_of_Code
