# Update nginx configuration
exec { 'update_nginx_config':
  command => '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx'
}

# Restart nginx service
exec { 'restart_nginx':
  command => '/usr/bin/env service nginx restart'
}
