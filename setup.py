from setuptools import setup

setup(
    name = "Badboy",
    version = "1.0.0",
    description = "A evil framework designed purely in Python",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/bad-boy",
    packages = ["soli"],
    entry_points = {
        'console_scripts': [
            'badboy = main:main'
        ]
    },
)