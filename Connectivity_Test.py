#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, timeit

def main():

    stmt = '''
    targetURLs = ('http://www.python.jp/doc/release/index.html',
        'http://www.python.jp/doc', #HTTPError, 301 Moved Permanently.
        'http://www.google.co.jp/',
        'http://ascii.jp/'
        )

    connectivity_test( targetURLs )
    '''

    t = timeit.Timer(stmt, "from __main__ import connectivity_test")

    print t.timeit(20)


def connectivity_test( targetURLs ):
    for url in targetURLs:
        try:
            r = urllib2.urlopen(url)
            print r.code
            print r.msg
        except urllib2.HTTPError, e:
            print e.code
            print e.msg
        except urllib2.URLError, e: # サーバに接続できない場合に発生
            print e

if __name__ == "__main__":
    main()