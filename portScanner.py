#!/usr/bin/python3

# Gregor Luedi
# 18.9.2014


def splitRanges(portlist,n):
	list_of_ranges =[]
	for i in range(n):
		list_of_ranges.append(portlist[i::n])
	return list_of_ranges



