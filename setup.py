from setuptools import setup

setup(
    name = 'yt',
    version = '0.1',
    py_modules = [
        "main"
    ],
    entry_points = {
        "console_scripts" : [
            "yt = main:cli"
        ]
    },
    author = "christian muwa",
    description = "a python tui for downloading audio and video form youtube",
    install_requires = [
        "ytube_api",
        "typer"
    ]
 )
