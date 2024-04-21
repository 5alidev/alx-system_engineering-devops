# Client configuration file (w/ Puppet)

file { '~/.ssh/config':
  ensure  => present,
  mode    => '0600',
  content => "
    Host *
      PasswordAuthentication no
      IdentityFile ~/.ssh/school
  ",
}
