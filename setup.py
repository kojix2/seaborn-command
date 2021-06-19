from setuptools import find_packages, setup

def read(path):
    with open(path, 'r') as f:
        return f.read()

setup(
    name='sns',
    version='0.0.1',
    description='seaborn command line tool',
    long_description=read('README.md'),
    author='kojix2',
    author_email='2xijok@gmail.com',
    install_requires=['seaborn', 'pandas'],
    entry_points={
        'console_scripts': ['sns=sns.main:main'],
    },
    url='https://github.com/kojix2/sns',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)