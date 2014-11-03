from setuptools import setup, find_packages

setup(
    name = "Greenspace",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greenspace'],
    install_requires = ['argparse']
)