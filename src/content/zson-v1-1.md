Title: What's new in ZSON v1.1?
Category: PostgreSQL
Date: 2017-06-02 16:00
Modified: 2017-06-02 16:00
Slug: zson-v1-1

ZSON v1.1 was released recently. Changes since v1.0:

* Bugfix: zson\_dict table used to be excluded from backups created via pg\_dump
  utility (see [a0d4201e][p1] and [e176165b][p2]). Reported by Pavel Luzanov;
* Bugfix: `make installcheck` used to fail on MacOS (see [b3a70915][p3]).
  Reported by Oleg Bartunov;
* Grammar fixes in the documentation (see [ceb9d5ee][p4] and [13cd5a69][p5]).
  Maria Popova;
* And various minor changes;

The following people contributed to this release one way or another (in random
order): Peder Rindal Refsnes, Maria Popova, Oleg Bartunov, Maxim Milyutin,
Dmitriy Olshevskiy, madisonleavo, Vyacheslav Semushin, Sergey Bronnikov, Marco
Craveiro, Madis Lõhmus, Pavel Luzanov.

[ZSON][zson] is a PostgreSQL extension for transparent JSONB compression. The
compression is based on the common dictionary of strings that are frequently
used in JSONB documents. In some cases ZSON can significantly reduce the
database size and improve the overall performance. For more details see [this
benchmark][bm]. ZSON is an open source software distributed under the MIT
license.

[p1]: https://github.com/postgrespro/zson/commit/a0d4201e0e3d021d9384a5d0a58c176be4c00735
[p2]: https://github.com/postgrespro/zson/commit/e176165bcff308dbeb02f16278f3b56f3f6e02d8
[p3]: https://github.com/postgrespro/zson/commit/b3a709153f132c6a586cf27fcbd4024a62cf7cba
[p4]: https://github.com/postgrespro/zson/commit/ceb9d5ee92bbaaaf129698c70a41662dd97b8e67
[p5]: https://github.com/postgrespro/zson/commit/13cd5a69cf5a7821202fa9bc2620d85140095f22
[zson]: https://github.com/postgrespro/zson
[bm]: https://github.com/postgrespro/zson/blob/master/docs/benchmark.md
