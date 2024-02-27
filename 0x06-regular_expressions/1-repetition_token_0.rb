#!/usr/bin/env ruby
# regular expresion for hbt{more than once}n

pattern = /hbt{2,5}n/
arg = ARGV[0]

puts arg.match(pattern)
