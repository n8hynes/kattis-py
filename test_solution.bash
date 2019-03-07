#!/bin/bash
# Tests solution
# $1 - problem name

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

Help text here

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

	

}

main "${@}"

