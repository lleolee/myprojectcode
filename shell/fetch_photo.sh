#/bin/bash
#file:fetch_email.sh
#function:test email receive




if [ $# -ne 3 ];
then
	echo "$0  URL -d DIRECTORY"
	exit 0
fi

username=""
password=""

SHOW_COUNT=5


for i in {1..4}
do
	case $1 in 
		-d) shift; directory=$1;shift;;
		*) url=${url:-$1};shift;;
	esac
done

echo "dirctory=$directory"
echo "url=$url"


mkdir -p $directory;
#echo $url |egrep -o "https?://[a-z.]+" > aa

baseurl=$(echo $url |egrep -o "https?://[a-z.]+")

echo "baseurl:$baseurl"
rm -f /tmp/*.list
curl -s $url |egrep -o "<img src=[^>]*>" |sed 's/<img src=\"\([^"]*\).*/\1/g' > /tmp/$$.list

sed -i "s|^//|http://|" /tmp/$$.list
sed -i "s|^/|$baseurl/|" /tmp/$$.list

cd $directory;
rm -f ./*


while read filename ;
do
	echo  filename=${filename##*/}
	echo  filename=${filename}
	curl -s O "$filename" --silent > "`pwd`/${filename##*/}"
	echo  wget###filename=${filename}
	wget "$filename"
	echo "savetofile:`pwd`/${filename##*/}"

done < /tmp/$$.list

if [ $? -eq 0 ];
then
	echo "SECCESS"
else
	echo "FAIL"
fi
