# Puppet manifest to install Flask version 2.1.0 using pip3

# Install Flask using pip3 with the specified version
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
