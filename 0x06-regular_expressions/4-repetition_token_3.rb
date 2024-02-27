#!/usr/bin/env ruby
# regex for hbtn with t appears 0 times or more


pattern = /hbt*n/
arg = ARGV[0]

puts arg.match(pattern)
