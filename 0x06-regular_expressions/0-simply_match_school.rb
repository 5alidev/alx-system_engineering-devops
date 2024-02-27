#!/usr/bin/env ruby
# check if The regular expression must match School

pattern = /School/
arg = ARGV[0]

matches = arg.scan(pattern)

puts matches.join
