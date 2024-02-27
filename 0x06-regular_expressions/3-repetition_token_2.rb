#!/usr/bin/env ruby
# regex for hbt{1 or 4 times max}n

pattern = /hbt{1,4}n/
arg = ARGV[0]

puts arg.match(pattern)
