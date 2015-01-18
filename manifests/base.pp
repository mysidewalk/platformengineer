exec { 'apt-get update':
  command => '/usr/bin/apt-get update'
}

package {"nginx":
    ensure => present,
    require => Exec['apt-get update']
}
