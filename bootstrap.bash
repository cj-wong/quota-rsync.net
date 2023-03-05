#!/usr/bin/env bash
#
# Bootstrap the installation of requirements.
#

script_dir="$(dirname "${BASH_SOURCE[0]}")"

if ! cd "$script_dir"; then
    echo "Could not enter script dir" >&2
    exit 1
fi

env="${script_dir}/.venv"
printf '%s\n' "Creating a virtual environment at ${env}"

if [[ -e "${env}/bin/activate" ]]; then
    printf '%s\n' "
It appears that you already have a virtual environment.
Dependencies won't be installed." >&2

else
    python3 -m venv "$env"

    # shellcheck disable=SC1091
    # The script only exists conditionally.
    . "${env}/bin/activate"

    pip install -r "${script_dir}/requirements.txt"
    printf '\n%s\n' "Successfully installed dependencies."

    deactivate
fi

echo

printf '%s\n' "Creating systemd service files"
systemd_user="${XDG_CONFIG_HOME:-${HOME}/.config}/systemd/user"
mkdir -p "${systemd_user}"

systemd_prefix="quota-rsync.net"

for file in service timer; do
    full_file="${systemd_prefix}.${file}"
    systemd_file="${systemd_user}/${full_file}"

    if [[ -e "$systemd_file" ]]; then
        printf '%s\n' "${systemd_file} already exists." >&2

    else
        PATH_TO_THIS_REPO="$(pwd)"
        export PATH_TO_THIS_REPO
        envsubst "\$PATH_TO_THIS_REPO" < "resources/${full_file}" \
            > "$systemd_file"
        printf '%s\n' "Installed ${full_file}"
    fi
done

printf '%s\n' "
To enable the systemd service, run the following:

    systemctl --user daemon-reload
    systemctl --user enable ${systemd_prefix}.timer --now

Bootstrap is complete."
