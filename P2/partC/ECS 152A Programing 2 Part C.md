ECS 152A Programing 2 Part C

a.

First command:

```
dig +norecurse @a.root-servers.net any cs.ucdavis.edu
```

First response :

```

; <<>> DiG 9.11.3-1ubuntu1.14-Ubuntu <<>> +norecurse @a.root-servers.net any cs.ucdavis.edu
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 48607
;; flags: qr; QUERY: 1, ANSWER: 0, AUTHORITY: 13, ADDITIONAL: 27

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;cs.ucdavis.edu.			IN	ANY

;; AUTHORITY SECTION:
edu.			172800	IN	NS	b.edu-servers.net.
edu.			172800	IN	NS	f.edu-servers.net.
edu.			172800	IN	NS	i.edu-servers.net.
edu.			172800	IN	NS	a.edu-servers.net.
edu.			172800	IN	NS	g.edu-servers.net.
edu.			172800	IN	NS	j.edu-servers.net.
edu.			172800	IN	NS	k.edu-servers.net.
edu.			172800	IN	NS	m.edu-servers.net.
edu.			172800	IN	NS	l.edu-servers.net.
edu.			172800	IN	NS	h.edu-servers.net.
edu.			172800	IN	NS	c.edu-servers.net.
edu.			172800	IN	NS	e.edu-servers.net.
edu.			172800	IN	NS	d.edu-servers.net.

;; ADDITIONAL SECTION:
b.edu-servers.net.	172800	IN	A	192.33.14.30
b.edu-servers.net.	172800	IN	AAAA	2001:503:231d::2:30
f.edu-servers.net.	172800	IN	A	192.35.51.30
f.edu-servers.net.	172800	IN	AAAA	2001:503:d414::30
i.edu-servers.net.	172800	IN	A	192.43.172.30
i.edu-servers.net.	172800	IN	AAAA	2001:503:39c1::30
a.edu-servers.net.	172800	IN	A	192.5.6.30
a.edu-servers.net.	172800	IN	AAAA	2001:503:a83e::2:30
g.edu-servers.net.	172800	IN	A	192.42.93.30
g.edu-servers.net.	172800	IN	AAAA	2001:503:eea3::30
j.edu-servers.net.	172800	IN	A	192.48.79.30
j.edu-servers.net.	172800	IN	AAAA	2001:502:7094::30
k.edu-servers.net.	172800	IN	A	192.52.178.30
k.edu-servers.net.	172800	IN	AAAA	2001:503:d2d::30
m.edu-servers.net.	172800	IN	A	192.55.83.30
m.edu-servers.net.	172800	IN	AAAA	2001:501:b1f9::30
l.edu-servers.net.	172800	IN	A	192.41.162.30
l.edu-servers.net.	172800	IN	AAAA	2001:500:d937::30
h.edu-servers.net.	172800	IN	A	192.54.112.30
h.edu-servers.net.	172800	IN	AAAA	2001:502:8cc::30
c.edu-servers.net.	172800	IN	A	192.26.92.30
c.edu-servers.net.	172800	IN	AAAA	2001:503:83eb::30
e.edu-servers.net.	172800	IN	A	192.12.94.30
e.edu-servers.net.	172800	IN	AAAA	2001:502:1ca1::30
d.edu-servers.net.	172800	IN	A	192.31.80.30
d.edu-servers.net.	172800	IN	AAAA	2001:500:856e::30

;; Query time: 9 msec
;; SERVER: 2001:503:ba3e::2:30#53(2001:503:ba3e::2:30)
;; WHEN: Wed Mar 03 16:16:33 PST 2021
;; MSG SIZE  rcvd: 838
```

Second Command:

```
dig +norecurse @b.edu-servers.net any cs.ucdavis.edu
```

Second Result:

```

; <<>> DiG 9.11.3-1ubuntu1.14-Ubuntu <<>> +norecurse @b.edu-servers.net any cs.ucdavis.edu
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 21292
;; flags: qr; QUERY: 1, ANSWER: 0, AUTHORITY: 3, ADDITIONAL: 7

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;cs.ucdavis.edu.			IN	ANY

;; AUTHORITY SECTION:
ucdavis.edu.		172800	IN	NS	dns-two.ucdavis.edu.
ucdavis.edu.		172800	IN	NS	dns-one.ucdavis.edu.
ucdavis.edu.		172800	IN	NS	dns-three.ucdavis.edu.

;; ADDITIONAL SECTION:
dns-two.ucdavis.edu.	172800	IN	A	128.120.252.10
dns-two.ucdavis.edu.	172800	IN	AAAA	2607:f810:3f0:2::2
dns-one.ucdavis.edu.	172800	IN	A	128.120.252.9
dns-one.ucdavis.edu.	172800	IN	AAAA	2607:f810:3f0:1::1
dns-three.ucdavis.edu.	172800	IN	A	169.237.243.171
dns-three.ucdavis.edu.	172800	IN	AAAA	2607:f810:ce0:10::2

;; Query time: 71 msec
;; SERVER: 2001:503:231d::2:30#53(2001:503:231d::2:30)
;; WHEN: Wed Mar 03 16:19:59 PST 2021
;; MSG SIZE  rcvd: 243


```

Third Command:

```
dig +norecurse @dns-two.ucdavis.edu any cs.ucdavis.edu
```

Third Response:

```

; <<>> DiG 9.11.3-1ubuntu1.14-Ubuntu <<>> +norecurse @dns-two.ucdavis.edu any cs.ucdavis.edu
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 50119
;; flags: qr aa ra; QUERY: 1, ANSWER: 10, AUTHORITY: 0, ADDITIONAL: 8

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
; COOKIE: f87b880d7c8ec3bfd9d0363b604027f008ce4678825de2df (good)
;; QUESTION SECTION:
;cs.ucdavis.edu.			IN	ANY

;; ANSWER SECTION:
cs.ucdavis.edu.		28800	IN	SOA	infoblox.ucdavis.edu. netadmin.ucdavis.edu. 99033107 10800 900 1209600 900
cs.ucdavis.edu.		28800	IN	MX	5 sfire.cs.ucdavis.edu.
cs.ucdavis.edu.		28800	IN	TXT	"v=spf1 ip4:169.237.6.1 ip4:169.237.6.11 include:_spf.google.com ~all"
cs.ucdavis.edu.		28800	IN	A	151.101.2.132
cs.ucdavis.edu.		28800	IN	A	151.101.194.132
cs.ucdavis.edu.		28800	IN	A	151.101.66.132
cs.ucdavis.edu.		28800	IN	A	151.101.130.132
cs.ucdavis.edu.		28800	IN	NS	dns-two.ucdavis.edu.
cs.ucdavis.edu.		28800	IN	NS	dns-three.ucdavis.edu.
cs.ucdavis.edu.		28800	IN	NS	dns-one.ucdavis.edu.

;; ADDITIONAL SECTION:
dns-three.ucdavis.edu.	14400	IN	AAAA	2607:f810:ce0:10::2
dns-one.ucdavis.edu.	14400	IN	AAAA	2607:f810:3f0:1::1
dns-two.ucdavis.edu.	14400	IN	AAAA	2607:f810:3f0:2::2
sfire.cs.ucdavis.edu.	28800	IN	A	169.237.6.1
dns-three.ucdavis.edu.	14400	IN	A	169.237.243.171
dns-one.ucdavis.edu.	14400	IN	A	128.120.252.9
dns-two.ucdavis.edu.	14400	IN	A	128.120.252.10

;; Query time: 3 msec
;; SERVER: 2607:f810:3f0:2::2#53(2607:f810:3f0:2::2)
;; WHEN: Wed Mar 03 16:21:04 PST 2021
;; MSG SIZE  rcvd: 508


```

List of the DNS servers in the delegation chain:

```
a.root-servers.net

b.edu-servers.net

dns-two.ucdavis.edu
```



b.

​	Google:

​	First command:

```
dig +norecurse @a.root-servers.net any google.com
```

​	First result:

```

; <<>> DiG 9.11.3-1ubuntu1.14-Ubuntu <<>> +norecurse @a.root-servers.net any www.google.com
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 59902
;; flags: qr; QUERY: 1, ANSWER: 0, AUTHORITY: 13, ADDITIONAL: 27

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;www.google.com.			IN	ANY

;; AUTHORITY SECTION:
com.			172800	IN	NS	e.gtld-servers.net.
com.			172800	IN	NS	b.gtld-servers.net.
com.			172800	IN	NS	j.gtld-servers.net.
com.			172800	IN	NS	m.gtld-servers.net.
com.			172800	IN	NS	i.gtld-servers.net.
com.			172800	IN	NS	f.gtld-servers.net.
com.			172800	IN	NS	a.gtld-servers.net.
com.			172800	IN	NS	g.gtld-servers.net.
com.			172800	IN	NS	h.gtld-servers.net.
com.			172800	IN	NS	l.gtld-servers.net.
com.			172800	IN	NS	k.gtld-servers.net.
com.			172800	IN	NS	c.gtld-servers.net.
com.			172800	IN	NS	d.gtld-servers.net.

;; ADDITIONAL SECTION:
e.gtld-servers.net.	172800	IN	A	192.12.94.30
e.gtld-servers.net.	172800	IN	AAAA	2001:502:1ca1::30
b.gtld-servers.net.	172800	IN	A	192.33.14.30
b.gtld-servers.net.	172800	IN	AAAA	2001:503:231d::2:30
j.gtld-servers.net.	172800	IN	A	192.48.79.30
j.gtld-servers.net.	172800	IN	AAAA	2001:502:7094::30
m.gtld-servers.net.	172800	IN	A	192.55.83.30
m.gtld-servers.net.	172800	IN	AAAA	2001:501:b1f9::30
i.gtld-servers.net.	172800	IN	A	192.43.172.30
i.gtld-servers.net.	172800	IN	AAAA	2001:503:39c1::30
f.gtld-servers.net.	172800	IN	A	192.35.51.30
f.gtld-servers.net.	172800	IN	AAAA	2001:503:d414::30
a.gtld-servers.net.	172800	IN	A	192.5.6.30
a.gtld-servers.net.	172800	IN	AAAA	2001:503:a83e::2:30
g.gtld-servers.net.	172800	IN	A	192.42.93.30
g.gtld-servers.net.	172800	IN	AAAA	2001:503:eea3::30
h.gtld-servers.net.	172800	IN	A	192.54.112.30
h.gtld-servers.net.	172800	IN	AAAA	2001:502:8cc::30
l.gtld-servers.net.	172800	IN	A	192.41.162.30
l.gtld-servers.net.	172800	IN	AAAA	2001:500:d937::30
k.gtld-servers.net.	172800	IN	A	192.52.178.30
k.gtld-servers.net.	172800	IN	AAAA	2001:503:d2d::30
c.gtld-servers.net.	172800	IN	A	192.26.92.30
c.gtld-servers.net.	172800	IN	AAAA	2001:503:83eb::30
d.gtld-servers.net.	172800	IN	A	192.31.80.30
d.gtld-servers.net.	172800	IN	AAAA	2001:500:856e::30

;; Query time: 9 msec
;; SERVER: 2001:503:ba3e::2:30#53(2001:503:ba3e::2:30)
;; WHEN: Wed Mar 03 16:37:53 PST 2021
;; MSG SIZE  rcvd: 839


```

Second command:

```
dig +norecurse @e.gtld-servers.net any google.com
```

Second result:

```

; <<>> DiG 9.11.3-1ubuntu1.14-Ubuntu <<>> +norecurse @e.gtld-servers.net any www.google.com
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 10256
;; flags: qr; QUERY: 1, ANSWER: 0, AUTHORITY: 4, ADDITIONAL: 9

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;www.google.com.			IN	ANY

;; AUTHORITY SECTION:
google.com.		172800	IN	NS	ns2.google.com.
google.com.		172800	IN	NS	ns1.google.com.
google.com.		172800	IN	NS	ns3.google.com.
google.com.		172800	IN	NS	ns4.google.com.

;; ADDITIONAL SECTION:
ns2.google.com.		172800	IN	AAAA	2001:4860:4802:34::a
ns2.google.com.		172800	IN	A	216.239.34.10
ns1.google.com.		172800	IN	AAAA	2001:4860:4802:32::a
ns1.google.com.		172800	IN	A	216.239.32.10
ns3.google.com.		172800	IN	AAAA	2001:4860:4802:36::a
ns3.google.com.		172800	IN	A	216.239.36.10
ns4.google.com.		172800	IN	AAAA	2001:4860:4802:38::a
ns4.google.com.		172800	IN	A	216.239.38.10

;; Query time: 23 msec
;; SERVER: 2001:502:1ca1::30#53(2001:502:1ca1::30)
;; WHEN: Wed Mar 03 16:38:52 PST 2021
;; MSG SIZE  rcvd: 291


```

Third command:

```
dig +norecurse @ns2.google.com any google.com
```

Third result:

```

; <<>> DiG 9.11.3-1ubuntu1.14-Ubuntu <<>> +norecurse @ns2.google.com any www.google.com
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 5951
;; flags: qr aa; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;www.google.com.			IN	ANY

;; ANSWER SECTION:
www.google.com.		300	IN	A	172.217.6.68
www.google.com.		300	IN	AAAA	2607:f8b0:4005:80a::2004

;; Query time: 18 msec
;; SERVER: 2001:4860:4802:34::a#53(2001:4860:4802:34::a)
;; WHEN: Wed Mar 03 16:39:30 PST 2021
;; MSG SIZE  rcvd: 87


```

​	Google delegation chain:

```
a.root-servers.net
e.gtld-servers.net
ns2.google.com
```

​	

​	Yahoo:

​	First command:

```
dig +norecurse @a.root-servers.net any yahoo.com
```

​	First output:

```

; <<>> DiG 9.11.3-1ubuntu1.14-Ubuntu <<>> +norecurse @a.root-servers.net any www.yahoo.com
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 50329
;; flags: qr; QUERY: 1, ANSWER: 0, AUTHORITY: 13, ADDITIONAL: 27

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;www.yahoo.com.			IN	ANY

;; AUTHORITY SECTION:
com.			172800	IN	NS	e.gtld-servers.net.
com.			172800	IN	NS	b.gtld-servers.net.
com.			172800	IN	NS	j.gtld-servers.net.
com.			172800	IN	NS	m.gtld-servers.net.
com.			172800	IN	NS	i.gtld-servers.net.
com.			172800	IN	NS	f.gtld-servers.net.
com.			172800	IN	NS	a.gtld-servers.net.
com.			172800	IN	NS	g.gtld-servers.net.
com.			172800	IN	NS	h.gtld-servers.net.
com.			172800	IN	NS	l.gtld-servers.net.
com.			172800	IN	NS	k.gtld-servers.net.
com.			172800	IN	NS	c.gtld-servers.net.
com.			172800	IN	NS	d.gtld-servers.net.

;; ADDITIONAL SECTION:
e.gtld-servers.net.	172800	IN	A	192.12.94.30
e.gtld-servers.net.	172800	IN	AAAA	2001:502:1ca1::30
b.gtld-servers.net.	172800	IN	A	192.33.14.30
b.gtld-servers.net.	172800	IN	AAAA	2001:503:231d::2:30
j.gtld-servers.net.	172800	IN	A	192.48.79.30
j.gtld-servers.net.	172800	IN	AAAA	2001:502:7094::30
m.gtld-servers.net.	172800	IN	A	192.55.83.30
m.gtld-servers.net.	172800	IN	AAAA	2001:501:b1f9::30
i.gtld-servers.net.	172800	IN	A	192.43.172.30
i.gtld-servers.net.	172800	IN	AAAA	2001:503:39c1::30
f.gtld-servers.net.	172800	IN	A	192.35.51.30
f.gtld-servers.net.	172800	IN	AAAA	2001:503:d414::30
a.gtld-servers.net.	172800	IN	A	192.5.6.30
a.gtld-servers.net.	172800	IN	AAAA	2001:503:a83e::2:30
g.gtld-servers.net.	172800	IN	A	192.42.93.30
g.gtld-servers.net.	172800	IN	AAAA	2001:503:eea3::30
h.gtld-servers.net.	172800	IN	A	192.54.112.30
h.gtld-servers.net.	172800	IN	AAAA	2001:502:8cc::30
l.gtld-servers.net.	172800	IN	A	192.41.162.30
l.gtld-servers.net.	172800	IN	AAAA	2001:500:d937::30
k.gtld-servers.net.	172800	IN	A	192.52.178.30
k.gtld-servers.net.	172800	IN	AAAA	2001:503:d2d::30
c.gtld-servers.net.	172800	IN	A	192.26.92.30
c.gtld-servers.net.	172800	IN	AAAA	2001:503:83eb::30
d.gtld-servers.net.	172800	IN	A	192.31.80.30
d.gtld-servers.net.	172800	IN	AAAA	2001:500:856e::30

;; Query time: 9 msec
;; SERVER: 2001:503:ba3e::2:30#53(2001:503:ba3e::2:30)
;; WHEN: Wed Mar 03 16:40:14 PST 2021
;; MSG SIZE  rcvd: 838


```

Second command:

```
dig +norecurse @e.gtld-servers.net any yahoo.com
```

Second output:

```

; <<>> DiG 9.11.3-1ubuntu1.14-Ubuntu <<>> +norecurse @e.gtld-servers.net any www.yahoo.com
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 28664
;; flags: qr; QUERY: 1, ANSWER: 0, AUTHORITY: 5, ADDITIONAL: 10

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;www.yahoo.com.			IN	ANY

;; AUTHORITY SECTION:
yahoo.com.		172800	IN	NS	ns1.yahoo.com.
yahoo.com.		172800	IN	NS	ns5.yahoo.com.
yahoo.com.		172800	IN	NS	ns2.yahoo.com.
yahoo.com.		172800	IN	NS	ns3.yahoo.com.
yahoo.com.		172800	IN	NS	ns4.yahoo.com.

;; ADDITIONAL SECTION:
ns1.yahoo.com.		172800	IN	AAAA	2001:4998:130::1001
ns1.yahoo.com.		172800	IN	A	68.180.131.16
ns5.yahoo.com.		172800	IN	A	202.165.97.53
ns5.yahoo.com.		172800	IN	AAAA	2406:2000:ff60::53
ns2.yahoo.com.		172800	IN	AAAA	2001:4998:140::1002
ns2.yahoo.com.		172800	IN	A	68.142.255.16
ns3.yahoo.com.		172800	IN	AAAA	2406:8600:f03f:1f8::1003
ns3.yahoo.com.		172800	IN	A	27.123.42.42
ns4.yahoo.com.		172800	IN	A	98.138.11.157

;; Query time: 24 msec
;; SERVER: 2001:502:1ca1::30#53(2001:502:1ca1::30)
;; WHEN: Wed Mar 03 16:41:14 PST 2021
;; MSG SIZE  rcvd: 324


```

Third command:

```
dig +norecurse @ns1.yahoo.com any yahoo.com
```

Third output:

```

; <<>> DiG 9.11.3-1ubuntu1.14-Ubuntu <<>> +norecurse @ns1.yahoo.com any www.yahoo.com
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 25381
;; flags: qr aa; QUERY: 1, ANSWER: 1, AUTHORITY: 5, ADDITIONAL: 10

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1272
; COOKIE: 9d21a36b1e54511186f12ffa60402ccdaefae5c7f875c675 (good)
;; QUESTION SECTION:
;www.yahoo.com.			IN	ANY

;; ANSWER SECTION:
www.yahoo.com.		60	IN	CNAME	new-fp-shed.wg1.b.yahoo.com.

;; AUTHORITY SECTION:
yahoo.com.		172800	IN	NS	ns5.yahoo.com.
yahoo.com.		172800	IN	NS	ns2.yahoo.com.
yahoo.com.		172800	IN	NS	ns3.yahoo.com.
yahoo.com.		172800	IN	NS	ns1.yahoo.com.
yahoo.com.		172800	IN	NS	ns4.yahoo.com.

;; ADDITIONAL SECTION:
ns1.yahoo.com.		86400	IN	AAAA	2001:4998:130::1001
ns2.yahoo.com.		86400	IN	AAAA	2001:4998:140::1002
ns3.yahoo.com.		1800	IN	AAAA	2406:8600:f03f:1f8::1003
ns5.yahoo.com.		86400	IN	AAAA	2406:2000:ff60::53
ns1.yahoo.com.		1209600	IN	A	68.180.131.16
ns2.yahoo.com.		1209600	IN	A	68.142.255.16
ns3.yahoo.com.		1800	IN	A	27.123.42.42
ns4.yahoo.com.		1209600	IN	A	98.138.11.157
ns5.yahoo.com.		86400	IN	A	202.165.97.53

;; Query time: 7 msec
;; SERVER: 2001:4998:130::1001#53(2001:4998:130::1001)
;; WHEN: Wed Mar 03 16:41:49 PST 2021
;; MSG SIZE  rcvd: 384


```

Yahoo delegation chain:

```
a.root-servers.net
e.gtld-servers.net
ns1.yahoo.com
```



​	Amazon:

​	First command:

```
dig +norecurse @a.root-servers.net any amazon.com
```

​	First output:

```

; <<>> DiG 9.11.3-1ubuntu1.14-Ubuntu <<>> +norecurse @a.root-servers.net any amazon.com
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 38015
;; flags: qr; QUERY: 1, ANSWER: 0, AUTHORITY: 13, ADDITIONAL: 27

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;amazon.com.			IN	ANY

;; AUTHORITY SECTION:
com.			172800	IN	NS	a.gtld-servers.net.
com.			172800	IN	NS	b.gtld-servers.net.
com.			172800	IN	NS	c.gtld-servers.net.
com.			172800	IN	NS	d.gtld-servers.net.
com.			172800	IN	NS	e.gtld-servers.net.
com.			172800	IN	NS	f.gtld-servers.net.
com.			172800	IN	NS	g.gtld-servers.net.
com.			172800	IN	NS	h.gtld-servers.net.
com.			172800	IN	NS	i.gtld-servers.net.
com.			172800	IN	NS	j.gtld-servers.net.
com.			172800	IN	NS	k.gtld-servers.net.
com.			172800	IN	NS	l.gtld-servers.net.
com.			172800	IN	NS	m.gtld-servers.net.

;; ADDITIONAL SECTION:
a.gtld-servers.net.	172800	IN	A	192.5.6.30
b.gtld-servers.net.	172800	IN	A	192.33.14.30
c.gtld-servers.net.	172800	IN	A	192.26.92.30
d.gtld-servers.net.	172800	IN	A	192.31.80.30
e.gtld-servers.net.	172800	IN	A	192.12.94.30
f.gtld-servers.net.	172800	IN	A	192.35.51.30
g.gtld-servers.net.	172800	IN	A	192.42.93.30
h.gtld-servers.net.	172800	IN	A	192.54.112.30
i.gtld-servers.net.	172800	IN	A	192.43.172.30
j.gtld-servers.net.	172800	IN	A	192.48.79.30
k.gtld-servers.net.	172800	IN	A	192.52.178.30
l.gtld-servers.net.	172800	IN	A	192.41.162.30
m.gtld-servers.net.	172800	IN	A	192.55.83.30
a.gtld-servers.net.	172800	IN	AAAA	2001:503:a83e::2:30
b.gtld-servers.net.	172800	IN	AAAA	2001:503:231d::2:30
c.gtld-servers.net.	172800	IN	AAAA	2001:503:83eb::30
d.gtld-servers.net.	172800	IN	AAAA	2001:500:856e::30
e.gtld-servers.net.	172800	IN	AAAA	2001:502:1ca1::30
f.gtld-servers.net.	172800	IN	AAAA	2001:503:d414::30
g.gtld-servers.net.	172800	IN	AAAA	2001:503:eea3::30
h.gtld-servers.net.	172800	IN	AAAA	2001:502:8cc::30
i.gtld-servers.net.	172800	IN	AAAA	2001:503:39c1::30
j.gtld-servers.net.	172800	IN	AAAA	2001:502:7094::30
k.gtld-servers.net.	172800	IN	AAAA	2001:503:d2d::30
l.gtld-servers.net.	172800	IN	AAAA	2001:500:d937::30
m.gtld-servers.net.	172800	IN	AAAA	2001:501:b1f9::30

;; Query time: 8 msec
;; SERVER: 2001:503:ba3e::2:30#53(2001:503:ba3e::2:30)
;; WHEN: Wed Mar 03 16:42:46 PST 2021
;; MSG SIZE  rcvd: 835


```

​	Second command:

```
dig +norecurse @a.gtld-servers.net any amazon.com
```

​	Second output:

```

; <<>> DiG 9.11.3-1ubuntu1.14-Ubuntu <<>> +norecurse @a.gtld-servers.net any amazon.com
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 49758
;; flags: qr; QUERY: 1, ANSWER: 0, AUTHORITY: 6, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;amazon.com.			IN	ANY

;; AUTHORITY SECTION:
amazon.com.		172800	IN	NS	pdns1.ultradns.net.
amazon.com.		172800	IN	NS	pdns6.ultradns.co.uk.
amazon.com.		172800	IN	NS	ns1.p31.dynect.net.
amazon.com.		172800	IN	NS	ns3.p31.dynect.net.
amazon.com.		172800	IN	NS	ns2.p31.dynect.net.
amazon.com.		172800	IN	NS	ns4.p31.dynect.net.

;; Query time: 23 msec
;; SERVER: 2001:503:a83e::2:30#53(2001:503:a83e::2:30)
;; WHEN: Wed Mar 03 16:43:24 PST 2021
;; MSG SIZE  rcvd: 188


```

​	Amazon delegation chain:

```
a.root-servers.net
a.gtld-servers.net
```





