setup(
    name='sns',
    version='0.0.1',
    description='seaborn command line tool',
    long_description=readme,
    author='kojix2',
    author_email='2xijok@gmail.com',
    install_requires=['seaborn', 'pandas'],
    url='https://github.com/kojix2/sns',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)