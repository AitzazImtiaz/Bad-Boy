from setuptools import setup

setup(
    name = "Badboy",
    version = "1.0.0",
    description = "ls clone",
    author = "JeffTheK",
    url = "https://github.com/AitzazImtiaz/bad-boy",
    packages = ["soli"],
    entry_points = {
        'console_scripts': [
            'badboy = main:main'
        ]
    },
)
