Title: Back from PGCon 2017
Category: PostgreSQL
Date: 2017-05-29 14:00
Modified: 2017-05-29 14:00
Slug: pgcon2017

Last week my colleagues [Alexander Korotlkov][ak], [Teodor Sigaev][ts], Oleg
Ivanov and I have been in Ottawa, Canada on the [PGCon 2017][pgcon] conference.
Also Alexander Kukushkin ([Zalando][zl]) has joined and spent a lot of time
with us. I'm still having a jet lag (in my case second day is always the worst
one) so I'm having some difficulties poetically describing how great it was,
but I'll try.

![Canada 2017](/static/2017/canada2017.jpg)

_Alexander (back), Teodor (right), Oleg (front) and I (left) in Ottawa._

For me the most interesting part was to observe how open source community works
offline (developer meeting, unconference, ...) and to meet PostgreSQL
developers in person. Somehow it makes difference if you know that an email in
pgsql-hackers@ was sent not by just someone whose name doesn't tell you a lot,
but a real person you know, at least a little bit. Talks also were great.  I
personally most enjoyed [Corruption War Stories][cws] by Christophe Pettus and
[So You Want To Make An Extension?][ext] by Keith Fiske.

![PostgreSQL Dev Meeting 2017](/static/2017/devmeeting2017.jpg)

_[PGCon 2017 Developer Meeting 2017][dm] attendees. Photo by Dave Page.
[Source][src]._

I don't know for sure whose decision was to invite me on the developer meeting.
Maybe it's just an imposter syndrome (probably not), but I'm not considering
myself such a significant contributor to PostgreSQL. Anyway I would like to
thank that person or persons whoever he is or they are. I hope I didn't disturb
everyone too much ;)

On the developer meeting and later on the unconference I tried to figure out
whether it's possible to make PostgreSQL upgradable between major releases
without a downtime. The reason why I'm so interested in this particular topic is
that guys from [Yandex][ya] told me that this is probably the biggest problem
with PostgreSQL for them. [Here][upg] you can find a detailed post by Vladimir
Borodin on how they do an upgrade currently.

There was reached a consensus that despite the fact that it could be done in
theory the corresponding amount of work will be enormous, especially for a
relatively small open source community. To solve this problem every newer
version of PostgreSQL have to be backward compatible with catalog schema, tuples
format, pages format and replication protocol of the previous version. This
backward compatibility should be maintained and tested on every combination of
platform, compiler and configuration flags supported by PostgreSQL.
Concentrating on solving this problem by logical replication introduced in
PostgreSQL 10 seems to be much more practical.

Also I did a lightning talk "Data recovery using pg\_filedump". Here are the
slides:

<iframe src="//www.slideshare.net/slideshow/embed_code/key/mJ9av8zXwUlWwD" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

Unfortunately not many PostgreSQL users know about [pg\_filedump utility][fd]
and that it's capable of restoring data in format suitable for using in COPY FROM
queries (the feature I'm the one to blame for). TOAST is currently not supported
but it should work for everything else including in-page compression. If you
don't know the schema of the database you can restore it using pg\_filedump as
well. All this works even if PostgreSQL instance can't start and data is
partially corrupted. I hope that you'll never need this knowledge, but according
to Christophe's talk I mentioned above on rare occasions a tool like this can be
helpful.

And have you been on PGCon this year and if so what's your impression on the
conference?

[ak]: http://akorotkov.github.io/
[ts]: http://sigaev.ru/
[zl]: http://www.zalando.com/
[dm]: https://wiki.postgresql.org/wiki/PgCon\_2017\_Developer\_Meeting
[src]: https://www.facebook.com/groups/postgresql/permalink/601049913425093/
[cws]: http://www.pgcon.org/2017/schedule/events/1048.en.html
[ext]: http://www.pgcon.org/2017/schedule/events/1037.en.html
[pgcon]: http://www.pgcon.org/2017/
[ya]: https://yandex.com/company/
[upg]: https://simply.name/upgrading-postgres-to-9.4.html
[fd]: https://git.postgresql.org/gitweb/?p=pg_filedump.git;a=summary
