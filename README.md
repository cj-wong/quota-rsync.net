# Quota Logger for [rsync.net]

## Overview

This project logs quotas from your [rsync.net] account to sqlite3. The quotas are obtained through the remote command `quota`, usually executed like: `ssh rsync.net quota`.

## Usage

`python main.py [user_1 ...]`

Usernames are optional, but if one isn't supplied, the config must contain a username. See [Setup](#setup) below.

## Requirements

This code is designed around the following:

- Python 3.7+
    - `pendulum`

## Setup

1. Configure your `~/.ssh/config` file such that an entry for `rsync.net` exists, with the hostname filled. User can be optionally filled, as well. You should also already have `authorized_keys` set up on the remote, so that password-less login is available.

## Disclaimer

This project is not affiliated with or endorsed by [rsync.net]. See [LICENSE](LICENSE) for more detail.

[rsync.net]: https://www.rsync.net
