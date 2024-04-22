# Puppet manifest to create a file in /tmp

# Define file path
$file_path = '/tmp/school'

# Ensure the file is present with the specified content, permissions, owner, and group
file { $file_path:
  ensure  => present,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
