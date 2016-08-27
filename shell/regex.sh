#!/bin/bash
#file:regex.sh
#function:test regular expression


#regex mode

#word ( ?[a-zA-zA-z]+ ?)
#ip address [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}
#ip address [:digit:]{1,3}\.[:digit:]{1,3}\.[:digit:]{1,3}\.[:digit:]{1,3}

if [ $# -ne 1 ];
then
	echo "$0  filename"
	exit 0
fi

filename=$1

egrep -o "\b[[:alpha:]]+\b" $filename | \
awk '
{
	count[$0]++ 
}
END{ 
	printf("%-14s%s\n","Word","Count");
	for(ind in count){
		printf("%-14s%d\n",ind,count[ind]);
	}
}
'
if [ $? -eq 0 ];
then
	echo "the text exist in the file"
else
	echo "the text does not exist in the file"
fi
