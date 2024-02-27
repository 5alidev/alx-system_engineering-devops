#!/usr/bin/env ruby
# regex for only CAPITAL letters


pattern = /[A-Z]/
arg = ARGV[0]

puts arg.scan(pattern).join
