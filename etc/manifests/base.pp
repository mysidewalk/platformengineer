exec { 'apt-get update':
  command => '/usr/bin/apt-get update'
}

package {"nginx":
    ensure => present,
    require => Exec['apt-get update']
}

file {"remove-nginx-default-conf":
    path => '/etc/nginx/sites-enabled/default',
    ensure => absent,
    require => Package['nginx'],
}

file {"add-nginx-default-conf":
    path => '/etc/nginx/sites-enabled/training',
    ensure => present,
    require => Package['nginx'],
    source => "/vagrant/etc/nginx/training",
}
