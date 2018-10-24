#!/bin/bash

yum update -y
yum install httpd -y 
echo "Hello Terraform from" `curl http://169.254.169.254/latest/meta-data/local-ipv4` > /var/www/html/index.html
service httpd start
