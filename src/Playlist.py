#!usr/bin/python -tt
"""
Playlist.py
	A library for playlist manipulation.  
James Swoger (hugin0)
"""
import re

class Playlist:
	
	# regular expressions used to determine which type of playlist we are dealing with
	playlistM3U = re.compile(r'\#EXTM3U', re.IGNORECASE)
	playlistPLS = re.compile(r'\[playlist\]', re.IGNORECASEs)

	# regular expressions used to find each of the entries.  One each for M3U and PLS formats
	entryM3U = re.compile(r'^\#EXTINF:(-?\d+),(\w*)\n(\w+)', re.MULTILINE)
	entryPLS = re.compile(r'^File(\d+)\:(\w+)\nTitle\1:(\w*)\nLength\1:(-?\d+)', re.MULTILINE)
	
	def __init__(file):
		
		self.__file = file
		self.__type = self.guess_type()

	def set_file(file):
		self.__file = file

	def get_file():
		return self.__file

	def guess_type():
		

	def get_entries():


if __name__ == '__main__':

	test_file = argv[1]
