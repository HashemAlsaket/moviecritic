#!/usr/bin/env python

from pathlib import Path

from setuptools import setup


def _get_requirements():
    """Install `requirements.txt`."""
    req_list = []
    with Path("requirements.txt").open("r") as f:
        for line in f:
            req = line.strip()
            req_list.append(req)
    return req_list

requirements = _get_requirements()

if __name__ == "__main__":
    setup(
        name="moviecritic",
        install_requires=requirements
    )
