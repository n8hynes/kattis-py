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

	local directory="problems/${problem}"

	if [[ -d "${directory}" ]]; then
		cd "${directory}" || die "Cannot navigate to directory"
		if [[ -d "samples/" ]]; then
			local x=1
			for i in samples/*.in; do
				touch "output"
				touch "error"
				python "${problem}.py" < "$i" > "output" 2> "error"
				exit_status="$?"
				if [[ ${exit_status} != 0 ]]; then
					echo -e "\nTEST ${x}: RUNTIME ERROR"
					echo "STDERR:"
					cat "error"
				elif ! cmp -s "output" "${i:0:-3}.ans"; then
					echo -e "\nTEST ${x}: FAIL"
					echo "STDERR:"
					cat "error"
					echo "STDOUT:"
					cat "output"
					echo "EXPECTED:"
					cat "${i:0:-3}.ans"
				else
					echo -e "\nTEST ${x}: PASS"
				fi
				rm "output"
				rm "error"
				let x+=1
			done
		else
			echo "There are no sample files to test!"
		fi
	else
		echo "No such problem to test."
	fi

}

main "${@}"

