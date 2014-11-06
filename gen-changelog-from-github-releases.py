#!/usr/bin/env python2
import argparse
import json
import sys
import urllib2

parser = argparse.ArgumentParser(description='Turns Github release list into Changelog.md file.')
parser.add_argument('repo', metavar='user/repo', type=str,
                    help='Target repository in "user/repo" format')
args = parser.parse_args()

url = 'https://api.github.com/repos/%s/releases' % args.repo
j = json.loads(urllib2.urlopen(url).read())

releases = [ (d['tag_name'], d['body']) for d in j if not d['prerelease'] and not d['draft'] ]

for i, (version, body) in enumerate(releases):
  print version
  print
  print '\n'.join( "  " + l for l in body.splitlines() )

  if i != len(releases) - 1:
    print
