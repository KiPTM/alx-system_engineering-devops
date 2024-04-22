# Puppet manifest to kill a process named killmenow using pkill

exec { 'killmenow':
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true,
}
