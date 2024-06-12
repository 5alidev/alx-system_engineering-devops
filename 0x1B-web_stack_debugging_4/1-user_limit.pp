# Define a file with the desired open file limit
file { '/etc/security/limits.conf':
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "* soft nofile 1024\n* hard nofile 4096\n"
}
