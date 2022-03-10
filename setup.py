from setuptools import setup

setup(
    name = "Bad-Boy",
    version = "1.0.0",
    description = "A evil framework designed purely in Python",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/bad-boy",
    packages = ["Bad-Boy"],
    entry_points = {
        'console_scripts': [
            'Bad-Boy = main:main'
        ]
    },
)
