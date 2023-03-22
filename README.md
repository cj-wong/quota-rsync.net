# Quota Logger for [rsync.net]

## Overview

This project logs quotas from your [rsync.net] account to `sqlite3`. The quotas are obtained through the remote command `quota`, usually executed like: `ssh rsync.net quota`.

## Usage

```
usage: main.py [-h] [-d DIRECTORY] [users ...]

positional arguments:
  users

options:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        optional parent directory
```

Usernames are optional, but if one isn't supplied, the config must contain a username. See [Setup](#setup) below.

A configuration file can be provided as well. For an example, look at `config.json.example`. Note that even if a configuration file exists, its contents will be overridden by command line provided arguments. Specifically, if the user supplies options while executing the command, anything equivalent in `config.json` will be ignored.

## Requirements

This code was tested with the following:

- Python 3.10+
    - `pendulum`
- OpenSSH for calling a remote command

## Setup

1. Configure your `~/.ssh/config` file such that an entry for `rsync.net` exists, with the hostname filled. User can be optionally filled, as well. You should also already have `authorized_keys` set up on the remote, so that password-less login is available.

## Disclaimer

This project is not affiliated with or endorsed by [rsync.net]. See [LICENSE](LICENSE) for more detail.

[rsync.net]: https://www.rsync.net
