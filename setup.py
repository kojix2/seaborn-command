from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="seaborn-command",
    version="0.0.3",
    description="seaborn command line tool",
    long_description=long_description,
    author="kojix2",
    author_email="2xijok@gmail.com",
    install_requires=["seaborn", "pandas"],
    entry_points={"console_scripts": ["seaborn=seaborn_command.main:main"],},
    url="https://github.com/kojix2/seaborn-command",
    license='MIT',
    packages=find_packages(exclude=("tests", "docs")),
)
