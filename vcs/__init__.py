from typing import List
from subprocess import call


def git_config() -> None:
    call(
        [
            "git",
            "config",
            "--global",
            "user.email",
            "github-actions[bot]@users.noreply.github.com",
        ]
    )
    call(
        [
            "git",
            "confg",
            "--global",
            "user.name",
            "GitHub Action",
        ],
    )


def git_add(files: List[str]) -> None:
    call(["git", "add", *files])


def git_commit() -> None:
    call("git", "commit", "updated the pypi badge")
