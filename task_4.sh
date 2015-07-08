touch ip.txt status.txt;
cut -d ' ' -f1 access.txt | sort >ip.txt ;
sed -i '/^$/d' ip.txt ;
uniq -c -i ip.txt | sort -n >temp.txt;
mv temp.txt ip.txt;
echo  "LIST OF NO. OF HITS of DIFFERENT IP";
cat ip.txt;
cut -d '"' -f3 access.txt| cut -d ' ' -f2 | sort >status.txt;
sed -i '/^$/d' status.txt;
uniq -c -i status.txt | sort -n >temp.txt;
mv temp.txt status.txt;
echo  "LIST OF FREQUENCY OF STATUS CODE";
cat status.txt;

