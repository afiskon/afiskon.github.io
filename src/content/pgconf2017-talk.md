Title: PGConf.us 2017 "In-core Compression" Talk Slides
Category: PostgreSQL
Date: 2017-04-05 17:40
Modified: 2017-04-05 18:40
Slug: pgconf2017-talk

On [PGConf.us 2017](https://pgconf.us/conferences/2017) Anastasia Lubennikova
and I [presented](https://pgconf.us/conferences/2017/program/proposals/274) a
talk "In-core compression: how to shrink your database size in several times".
Slides for this talk are now [available on SlideShare](https://www.slideshare.net/afiskon/incore-compression-how-to-shrink-your-database-size-in-several-times):

<iframe src="//www.slideshare.net/slideshow/embed_code/key/nyLpzTWVMt2SB4" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

Here is a short description of the talk:

> Currently PostgreSQL doesn't compress data in many cases when it's possible
> and can significantly reduce not only disk and memory usage but also number
> of IO operations. A common view on this problem is that it can be solved on
> file system level. Unfortunately in Linux, which is probably a most commonly
> used server OS these days, corresponding file systems are either not yet
> ready for usage in production environment or can't achieve same compression
> ratio that can be achieved on DBMS level. In this talk we will present our
> patches that implement page compression on disk and, optionally, in memory;
> a [ZSON extension](https://github.com/postgrespro/zson) that implement
> transparent JSONB compression; in what situation it is better to use what
> kind of compression; and also discuss our experience of using compression in
> production environment.

Video recording will be available on 
[PGConf.us YouTube channel](https://www.youtube.com/pgconfus/) soon. More slides
for PGConf.us 2017 talks are available on
[PostgreSQL Wiki](https://wiki.postgresql.org/wiki/PgConfUS_Talks_2017).
Slides for previous years could be found there as well.
