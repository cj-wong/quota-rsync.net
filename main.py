import re
import sqlite3
import subprocess
import sys
from typing import Optional

import pendulum


NONALPHANUM = re.compile(r'[^a-z0-9]', re.IGNORECASE)
NOW = pendulum.now().to_rfc3339_string()
DB_INIT = """
CREATE TABLE IF NOT EXISTS QUOTA (
    DATE TEXT UNIQUE, FS TEXT, USAGE REAL, SOFT_QUOTA REAL,
    HARD_QUOTA REAL, FILES INTEGER)"""


def sanitize(thing: str) -> str:
    """Sanitize any string, removing all non-alphanumeric characters.

    Used for sanitizing usernames and table names.

    Args:
        thing (str): the string to sanitize

    Returns:
        str: the sanitized string

    """
    return NONALPHANUM.sub('', thing)


def retrieve_and_store_quota(user: Optional[str] = None) -> None:
    """Run the quota command and retrieve stdout.

    The quota data will be stored under db/, in a sqlite3 database with the
    username used.

    Args:
        user (Optional[str]): user if provided

    Raises:
        subprocess.CalledProcessError: the command did not successfully run

    """
    if not user:
        user_host = 'rsync.net'
    else:
        user_host = f'{user}@rsync.net'

    command = ['ssh', user_host, 'quota']
    process = subprocess.run(command, capture_output=True, check=True)

    output = process.stdout.decode('utf-8')
    title, header, *rows, note = output.strip().split('\n')
    file = sanitize(user or title.split()[-1])

    db = sqlite3.connect(f'db/{file}.db')
    cursor = db.cursor()
    cursor.execute(DB_INIT)

    for row in rows:
        if not row:
            continue

        fs, usage, soft_quota, hard_quota, files, *_ = row.split()
        cursor.execute(
            'INSERT INTO QUOTA VALUES (?, ?, ?, ?, ?, ?)',
            (NOW, fs, usage, soft_quota, hard_quota, files)
            )

        db.commit()
    db.close()


def main() -> None:
    """Run code to check quota of rsync.net account.

    Raises:
        RuntimeError: the command did not successfully run; potential errors:
            a. ssh is not installed
            b. ssh is not configured correctly
            c. ssh attempt was unauthorized

    """
    try:
        if not sys.argv[1:]:
            retrieve_and_store_quota()
        else:
            for user in sys.argv[1:]:
                retrieve_and_store_quota(user)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            """The command failed. Most likely SSH is not configured.
            If ssh is installed, does your config have rsync.net?"""
            ) from e


if __name__ == '__main__':
    main()
