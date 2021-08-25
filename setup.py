from setuptools import setup, find_packages

setup(
    name = 'nclock',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/nclock.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = 'nuru clock',
    install_requires = ['setuptools', "playsound"],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "nclock = nclock.nclock:main",
        ]
    }
)
