Title: Back from PGCon 2017
Category: PostgreSQL
Date: 2017-05-29 14:00
Modified: 2017-05-29 14:00
Slug: pgcon2017

Last week my colleagues [Alexander Korotkov][ak], [Teodor Sigaev][ts], Oleg
Ivanov and I were in Ottawa, Canada on the [PGCon 2017][pgcon] conference.  Also
Alexander Kukushkin ([Zalando][zl]) joined and spent a lot of time with us.  I'm
still having a jet lag (in my case second day is always the worst one) so I'm
having some difficulties poetically describing how great it was, but I'll try.

![Canada 2017](/static/2017/canada2017.jpg)

_Alexander (back), Teodor (right), Oleg (front) and I (left) in Ottawa._

For me the most interesting part was to observe how the open source community
works offline (the developer meeting, the unconference, etc) and to meet
PostgreSQL developers in person. Somehow it makes a difference if you know that
an email in pgsql-hackers@ was sent not by just someone whose name doesn't tell
you a lot, but a real person you know, at least a little bit. The talks also
were great.  I personally most enjoyed [Corruption War Stories][cws] by
Christophe Pettus and [So You Want To Make An Extension?][ext] by Keith Fiske.

![PostgreSQL Dev Meeting 2017](/static/2017/devmeeting2017.jpg)

_[PGCon 2017 Developer Meeting 2017][dm] attendees. Photo by Dave Page.
[Source][src]._

I don't know for sure whose decision it was to invite me to the developer
meeting.  Maybe it's just an imposter syndrome (probably not), but I'm not
considering myself such a significant contributor to PostgreSQL. Anyway I would
like to thank that person or persons whoever he/she is or they are. I hope I didn't
disturb anyone too much ;)

At the developer meeting and later at the unconference I tried to figure out
whether it's possible to make PostgreSQL upgradable between major releases
without a downtime. The reason why I'm so interested in this particular topic is
that [Yandex][ya] guys told me that this is probably the biggest problem with
PostgreSQL they have. [Here][upg] you can find a detailed post by Vladimir
Borodin on how they are doing an upgrade currently.

There was a consensus reached that despite the fact that it could be done in
theory the corresponding amount of work will be enormous, especially for a
relatively small open source community. To solve this problem every next version
of PostgreSQL has to be backward compatible with the catalog schema, tuples
format, pages format and replication protocol of the previous version. This
backward compatibility should be maintained and tested on every combination of
platform, compiler and configuration flags supported by PostgreSQL.
Concentrating on solving this problem with logical replication introduced in
PostgreSQL 10 seems to be much more practical.

Also, I did a lightning talk "Data recovery using pg\_filedump". Here are the
slides:

<iframe src="//www.slideshare.net/slideshow/embed_code/key/mJ9av8zXwUlWwD" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

Download: [pg-filedump-pgcon2017.pdf (175K)][dwnl]

Unfortunately, not many PostgreSQL users know about [pg\_filedump utility][fd]
and that it's capable of restoring data in the format suitable for using in COPY
FROM queries (the feature I'm the one to blame for). TOAST is currently not
supported but it should work for everything else including in-page compression.
If you don't know the schema of the database you can restore it using
pg\_filedump as well. All this works even if PostgreSQL instance can't start and
data is partially corrupted. I hope that you'll never need this knowledge, but
according to Christophe's talk I mentioned above on rare occasions a tool like
this can be helpful.

And have you been to PGCon this year and if so what's your impression of the
conference?

[ak]: http://akorotkov.github.io/
[ts]: http://sigaev.ru/
[zl]: http://www.zalando.com/
[dm]: https://wiki.postgresql.org/wiki/PgCon_2017_Developer_Meeting
[src]: https://www.facebook.com/groups/postgresql/permalink/601049913425093/
[cws]: http://www.pgcon.org/2017/schedule/events/1048.en.html
[ext]: http://www.pgcon.org/2017/schedule/events/1037.en.html
[pgcon]: http://www.pgcon.org/2017/
[ya]: https://yandex.com/company/
[upg]: https://simply.name/upgrading-postgres-to-9.4.html
[fd]: https://git.postgresql.org/gitweb/?p=pg_filedump.git;a=summary
[dwnl]: /static/2017/pg-filedump-pgcon2017.pdf
