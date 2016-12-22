from setuptools import setup, find_packages

requirements = []
with open('requirements.txt', 'r') as f:
    for line in f:
        requirements.append(line.strip())

setup(
    name='jgsnippets',
    version='0.1',
    description='A collection of classes and function often used by myself.',
    author='Johannes Gontrum',
    author_email='gontrum@me.com',
    url='https://github.com/jgontrum/jgsnippets',
    include_package_data=True,
    license='MIT',
    packages=find_packages(),
    install_requires=requirements
)
