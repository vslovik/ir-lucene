Crawling with httrack
==============================

Starting from a specific link on IMDB
Download all movie pages within a certain distance
Extract information from them


    $ mkdir pages/ && cd pages/
    $ httrack www.imdb.com/genre/fantasy          \
    -*                                          \
    +www.imdb.com/title/tt*[file]/*[]           \
    +www.imdb.com/title/tt*[file]/index.html*[] \
    -r3

www.imdb.com/genre/fantasy - startting address
-*  discard all URLs, except...
-r3 limit depth to 3

check downloaded pages with: find

Syntax of httrack filters
* any character
*[file]
*[path]
*[<< NN] size less than NN Kbytes
*[> PP] size mre than PP Kbytes
*[<< NN > PP]

Download more IMDB pages from:
http://bit.ly/1SYuht7


Indexing and search with Lucene
===============================

Internal representation of documents depends on the analyzer we use to parse them.
Examples:
    KeywordAnalyzer: whole input in one singole token (no tokenization)
    WhitespaceAnalyzer: split on spaces
    SimpleAnalyzer: split on non-letters + lowercase
    ClassicAnalyzer: splits according to a set of rules (basically, non-letters)
     + lowercase + stopword removal + normalization

WhitespaceAnalyzer:
Why  | did | Obama, | president | of | U.S.A., | spoke | at | NATO | summit?

SimpleAnalyzer:
why  | did | obama | president | of | u | s | a | spoke | at | nato | summit

ClassicAnalyzer:
why | obama | president | usa | spoke | nato | summit


Build a toy search engine
Read from input (one document per line)
Index with Lucene
Search with Lucene


Install Lucene
--------------------------------
$ sudo apt-get install pylucene


Index three documents:
----------------------------------
    Obama u.s.a. NATO
    obama usa N.A.T.O.
    the cat meows


run
(one doc per line,
terminate with double CTRL+D)
------------------------------------
    $ python create_index.py


Check that index is created
----------------------------------
$ ls -ltr test_index/
total 80
-rw-rw-r-- 1 marco marco  44 mar 11 23:43 _0.fdx
-rw-rw-r-- 1 marco marco  67 mar 11 23:43 _0.fdt
-rw-rw-r-- 1 marco marco  53 mar 11 23:43 _0.tis
-rw-rw-r-- 1 marco marco  35 mar 11 23:43 _0.tii
-rw-rw-r-- 1 marco marco   9 mar 11 23:43 _0.prx
-rw-rw-r-- 1 marco marco   9 mar 11 23:43 _0.nrm
-rw-rw-r-- 1 marco marco   8 mar 11 23:43 _0.frq
-rw-rw-r-- 1 marco marco  12 mar 11 23:43 _0.fnm
-rw-rw-r-- 1 marco marco  20 mar 11 23:43 segments.gen
-rw-rw-r-- 1 marco marco 262 mar 11 23:43 segments_1


Search for:
-----------------------------------
    cat
    u.s.a.
    OBAMA
    N.A.T.O.

start
------------------------------------

    $ python search_index.py


Replace WhitespaceAnalyzer with ClassicAnalyzer,
recreate index, try same queries


Get full code at:
http://bit.ly/212HUNl (Marco Cornolti)
