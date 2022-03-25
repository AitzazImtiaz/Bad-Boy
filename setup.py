from setuptools import setup

setup(
    name = "badboy",
    version = "0.1.0",
    description = "A evil version for evil people",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/Bad-Boy",
    packages = ["badboy"],
    entry_points = {
        'console_scripts': [
            'badboy = badboy.__main__:main'
        ]
    },
)
