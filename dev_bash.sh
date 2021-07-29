#!/bin/bash



input="bash_commands.txt"

while IFS= read -r line
do
	eval "$line"
done < "$input"


