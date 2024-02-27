#!/usr/bin/env ruby
# regex for h_n (starts with h, end with n, any single char can be in between)


pattern = /^h.n$/
arg = ARGV[0]

puts arg.match(pattern)
