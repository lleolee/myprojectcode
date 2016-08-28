#/bin/bash
#file:fetch_email.sh
#function:test email receive




#if [ $# -ne 1 ];
#then
#	echo "$0  filename"
#	exit 0
#fi

username=""
password=""

SHOW_COUNT=5

echo 

curl -u $username:$password --silent "http://mail.163.com" #| \
#tr -d '\n' |sed 's:</entry>:\n:g' #| \
#sed 's/.*<title>\(.*\)<\/title.*<author><name>\([^<]*\)<\/name><email>
#\([^<]*\).*/Author: \2 [\3] \nSubject: \1\n/g' | \
#head -n $(( $SHOW_COUNT * 3 ))

if [ $? -eq 0 ];
then
	echo "SECCESS"
else
	echo "FAIL"
fi
