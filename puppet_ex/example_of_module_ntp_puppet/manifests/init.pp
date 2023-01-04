class ntp {
  package { 'ntp':
    ensure => latest,
    }

  file { '/etc/ntp.conf':
    source => '/home/user/ntp.conf',
    replace => true,
    require => Package['ntp'],  # The file requires the ntp package
    notify => Service['ntp'],  # ntp service should be notify if the conf file changes
    }
  
  service { 'ntp':
    enable => true,
    ensure => running,
    require => File['/etc/ntp.conf'],  # The service requires the configuration file
    }
}

include ntp  # Calling ntp is the way to say puppet to apply the rules describe in a class
 
