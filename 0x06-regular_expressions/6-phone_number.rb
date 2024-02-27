#!/usr/bin/env ruby
# regex for 10 digit phone number


pattern = /^\d{10}$/
arg = ARGV[0]

puts arg.match(pattern)
