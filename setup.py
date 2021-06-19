def get_version() -> str:
    version_filepath = os.path.join(ROOT_DIR, PACKAGE_DIRNAME, 'version.py')
    with open(version_filepath) as f:
        for line in f:
            if line.startswith('__version__'):
                return line.strip().split()[-1][1:-1]
    assert False

setup(
    name='sns',
    version='get_version(),
    description='seaborn command line tool',
    long_description=readme,
    author='kojix2',
    author_email='2xijok@gmail.com',
    install_requires=['seaborn', 'pandas'],
    url='https://github.com/kojix2/sns',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)