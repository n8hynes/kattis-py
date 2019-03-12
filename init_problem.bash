#!/bin/bash
# Sets up workspace for solving Kattis problems with Python
# $1 - filename of problem

set -o pipefail

readonly __USAGE__="Usage: ./${0##*/} [--help] <problem_name>"

# Logs to STDERR and exits with status 1
# $1 - error message
function die {
	local message="${1}"; shift
	echo -e "ERROR: ${message}" >&2
	exit 1
}

function show_help {
	cat << EOF
${__USAGE__}

Creates a directory for the given Kattis problem name, creates a template,
and downloads sample data (if any). 

Results in directory: problems/<problem_name>/
With sample data in: problems/<problem_name>/samples/

EOF
}

function main {
	local problem=""
	while :; do
		case $1 in
			-h|-\?|--help)
				show_help
				exit
				;;
			*)
				if [[ -z ${1} ]]; then 
					break
				elif [[ -z ${problem} ]]; then
					problem="${1,,}"
				else
					die "Unknown option: ${1}\n${__USAGE__}"
				fi
		esac
		shift
	done

	if [[ -z ${problem} ]]; then
		die "Missing required argument: <problem_name>\n${__USAGE__}"
	fi

	# Create directory and copy template to directory:

	local filename="${problem}.py"
	local directory="problems/${problem}"
	mkdir -p "${directory}" || die "Failed to create directory."
	cp "TEMPLATE.py" "${directory}/${filename}" || die "Failed to copy template file."
	echo "Directory created."

	# Download sample data to directory:

	local url="http://open.kattis.com/problems/${problem}/file/statement/samples.zip"

	echo "Downloading samples."
	wget -nv -P "${directory}" "${url}" || die "Failed to download samples."
	echo "Download complete."
	echo "Unzipping samples."
	mkdir "${directory}/samples" || die "Failed to create samples directory."
	unzip "${directory}/samples.zip" -d "${directory}/samples" || die "Failed to unzip samples file."
	echo "Samples unzipped. Deleting 'Samples.zip'."
	rm "${directory}/samples.zip" || die "Failed to delete samples zip file."
	echo "Done!"
	vim "${directory}/${filename}"
}

main "${@}"

