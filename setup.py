import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mlops-models',
    version='1.0.0',
    packages=find_packages(exclude=["notebooks/*", "data/*", "tests*"]),
    include_package_data=True,
    license='Trade Secret',  # example license
    description='Service for ...',
    long_description=README,
    url='https://repo-link.com',
    author='My Name',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Trade Secret',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ],
)
