#!/usr/bin/env ruby
# regex for hb{0 or 1 times}tn

pattern = /hb{0,1}tn/
arg = ARGV[0]

puts arg.match(pattern)
