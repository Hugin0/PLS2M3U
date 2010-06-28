#!/usr/bin/python -tt

# pls2m3u.py
# James Swoger (hugin0)
#
# 	This script takes a PLS style playlist and converts it to an m3u style.
# 	takes a list of files, or a glob on the commandline
#	it names the m3u file, the same as the pls, except replacing the extention.
# 
# 	ex. pls2m3u.py [pls files]
# 

import sys, re
from Playlist import Playlist

def process(file):
	
	pls_file = file
	
	m3u_file = re.sub(r".pls$", ".m3u", pls_file)
	
	in_playlist = Playlist(pls_file)
	
	pls_entries = in_playlist.get_entries()
	
	output = [ "#EXTM3U\n" ]
	for entry in pls_entries:
		output.append( "#EXTINF:%s, %s\n%s\n" % (entry[3], entry[2], entry[1]) )
	
	print "Converting %s to %s" % ( pls_file, m3u_file )
	handle = open(m3u_file, 'w')
	handle.writelines(output)
	handle.close

if __name__ == '__main__':

	if len(sys.argv) < 2: 
		print "usage:\n    pls2m3u.py [pls file 1] [pls file 2] ..."
	else:
		files = sys.argv[1:]

		for each in files:
			process(each)
