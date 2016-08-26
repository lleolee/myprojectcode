#!/bin/bash
#file:regex.sh
#function:test regular expression


#regex mode

#word ( ?[a-zA-zA-z]+ ?)
#ip address [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}
#ip address [:digit:]{1,3}\.[:digit:]{1,3}\.[:digit:]{1,3}\.[:digit:]{1,3}

if [ $# -ne 2 ];
then
	echo "$0 match_text filename"
	exit 0
fi

match_text=$1
filename=$2

grep -q $match_text $filename

if [ $? -eq 0 ];
then
	echo "the text exist in the file"
else
	echo "the text does not exist in the file"
fi
