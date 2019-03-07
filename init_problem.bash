#!/bin/bash
# Sets up workspace for solving Kattis problems with Python
# $1: filename of problem

if [[ -n $1 ]]; then
	problem="${1,,}"
else
	echo "Please provide the problem name as an argument to this script."
	exit 1
fi

# Create directory and copy template to directory:

filename="$problem.py"
directory="problems/$problem"
mkdir -p "$directory" || exit 1
cp "TEMPLATE.py" "$directory/$filename"
echo "Directory created."

# Download sample data to directory:

url="http://open.kattis.com/problems/$problem/file/statement/samples.zip"

echo "Downloading samples."
wget -nv -P "$directory" "$url" || exit 1
echo "Download complete."
echo "Unzipping samples."
mkdir "$directory/samples"
unzip "$directory/samples.zip" -d "$directory/samples"
echo "Samples unzipped. Deleting 'Samples.zip'."
rm "$directory/samples.zip"
echo "Done!"
