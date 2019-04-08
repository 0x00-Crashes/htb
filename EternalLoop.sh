#!/bin/bash

while true; do
	zipArchives=`ls -l | grep zip | wc -l`
	if [[ $zipArchives -eq 0 ]]; then
		echo "[~>] No zip archive in directory"
		break
	elif [[ $zipArchives -ge 2 ]]; then
		echo "[~>] Too many zip files in directory"
		break
	elif [[ $zipArchives -eq 1 ]]; then
		file=`ls | grep *zip`
		pass=`unzip -l $file | grep zip | awk '{print  $4}' | cut -d "." -f 1`
		passFiles=`unzip -l $file | grep zip | awk '{print  $4}' | cut -d "." -f 1 | wc -l`
		if [[ $passFiles -gt 1 ]] ; then
			unzip -qq -P $pass $file
			rm $file
		elif [[ $passFiles -lt 2 ]]; then
			echo -e '\n\r[~>] Done\n'
			break
		fi
		echo -en "\r[~>] $i";
		i=$(($i+1))
	fi
done;
