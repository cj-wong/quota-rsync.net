#!/usr/bin/env bash
#
# Wrapper for main.py
#
# This script is necessary to get around the virtual environment when used in
# conjunction with systemd.
#

script_dir="$(dirname "${BASH_SOURCE[0]}")"
env="${script_dir}/.venv"

if [[ ! -e "${env}/bin/activate" ]]; then
    printf '%s\n' "The virtual environment is missing" >&2
    exit 1
fi

# shellcheck disable=SC1091
# The script only exists conditionally.
. "${env}/bin/activate"

python3 "${script_dir}/main.py"
