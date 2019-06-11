from setuptools import setup, find_packages

with open('README.md', 'r') as fp:
    long_description = fp.read()

setup(
    name='python_algorithms',
    version='0.1.0',
    description='Package containing data structures, algorithms, and mathematics examples'
                ' for practice purposes.',
    long_description=long_description,
    packages=find_packages(exclude=('tests', 'docs'))
)
