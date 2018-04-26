#!/usr/bin/env bash
# mysql commti
#mysql path
host="amazom.cxq7foc1svrl.ap-northeast-1.rds.amazonaws.com"
user="amaroot"
password="amazon.18"
mysql -h $host -u $user -p$password <<EOF
show databases;
use mysql;
show tables;
select * from user
EOF
exit;
