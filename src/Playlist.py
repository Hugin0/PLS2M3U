#!/usr/bin/python -tt
"""
Playlist.py
	A library for playlist manipulation.  
James Swoger (hugin0)
"""
import re, sys

class Playlist:
	
	# regular expressions used to determine which type of playlist we are dealing with
	playlistM3U = re.compile(r'\#EXTM3U', re.IGNORECASE)
	playlistPLS = re.compile(r'\[playlist\]', re.IGNORECASE)

	# regular expressions used to find each of the entries.  One each for M3U and PLS formats
	entryM3U = re.compile(r'^\#EXTINF:(-?\d+),(.*)\n(.+)', re.I)
	entryPLS = re.compile(r'File(\d+)=(.+)\nTitle\1=(.*)\nLength\1=(-?\d+)', re.I)
	
	def __init__(self, file):
		
		self.__file = file
		handle = open(self.__file, 'r')
		self.contents = handle.read()
		handle.close()

		self.guess_type()

	def set_file(self, file):
		self.__file = file

	def get_file(self):
		return self.__file

	def get_type(self):
		return self.__type

	def guess_type(self):
		if self.playlistM3U.search(self.contents): 
			self.__type = 'm3u'
		elif self.playlistPLS.search(self.contents):
			self.__type = 'pls'
		else :
			self.__type = 'unknown'

	def get_entries(self):
		if self.__type == 'pls':
			matches = self.entryPLS.findall(self.contents)
		elif self.__type == 'm3u':
			matches = self.entryM3U.findall(self.contents)
		else:
			matches = None

		return matches

if __name__ == '__main__':

	#TESTING SEQUENCE

	test_file = sys.argv[1]
	
	playlist = Playlist(test_file)

	entries = playlist.get_entries()

	print "playlist type is", playlist.get_type()
	for entry in entries:
		print entry
