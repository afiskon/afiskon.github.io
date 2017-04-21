Title: TLS: Not Actually Secure?
Category: General
Date: 2017-04-16 13:20
Modified: 2017-04-17 17:50
Slug: tls-is-not-secure

Here is a little observation I would like to share.

![Chromium says that TLS is secure](/static/2017/tls-github-pages.png)

Chromium says that the connection to my blog is secure. However, what does
"secure" mean? For instance, can someone conduct a MITM attack - intercept
cookies or modify pages content? Well, TLS should guard against such attacks.
In theory.

In practice who owns the TLS certificate? GitHub does. I didn't even see this
certificate. So GitHub can listen and modify the traffic. Turned out, it's
not "secure" but rather "secure\*".

Same reasoning applies to any cloud hosting, such as AWS, Google Cloud, Azure,
and others. Nothing prevents Amazon from reading any files on your EC2
instance, including TLS certificates, and conduct a MITM attack afterwards.

It's an interesting sensation - to discover that you are living in a dystopia
where <del>corporations found a brilliant way to crack cryptography and</del>
<del>apparently no one cares</del> [1] almost everyone willingly shares their
TLS certificates without realizing that. After all, we all trust Amazon and
GitHub. So it's OK, right?

Update: [1] As [rightly noted][u1] by Jonathan Hilgeman this was not very accurate.

[u1]: https://afiskon.github.io/tls-is-not-secure.html#comment-3259876904
