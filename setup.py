from setuptools import find_packages, setup
setup(
    name='tuyalib',
    packages=find_packages(include=['tuyalib']),
    version='0.1.0',
    install_requires=['colour', 'pycryptodome', 'requests'],
    description='A python library which is a wrapper for the tuya core api.',
    author='Paul Molczanski',
    license='MIT',
)