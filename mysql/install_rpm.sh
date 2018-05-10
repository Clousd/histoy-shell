#/usr/bin/bash
#
echo "install mysql80-community-release"
yum install  https://repo.mysql.com//mysql80-community-release-el7-1.noarch.rpm -y
yum update -y
yum-config-manager --disable mysql80-community
yum-config-manager --enable mysql57-community
echo "1.mysql55-community/x86_64(@)"
echo "2.mysql56-community/x86_64(#)"
echo "3.mysql57-community/x86_64(&)"
echo "3.mysql58-community/x86_64(&)"
echo Please choose:
#下面一行是换行
read -p "Select an option [1-4]: " option
	case $option in
		1)
   		echo "select 1 "
  		;;
   		2)
  		 echo "select 2"
   		;;
   	esac
