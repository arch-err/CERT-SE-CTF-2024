#!/usr/bin/env bash

while read line; do
	if ! grep -qi $line $rockyou; then
		echo $line
	fi

done < lower.txt
