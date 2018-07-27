from setuptools import setup
from setuptools import find_packages

print(find_packages())
setup(
    name="socr",
    version="0.0",
    author="Senan Kelly",
    author_email="senan@senan.xyz",
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points = {
        'console_scripts': [
          'socr = socr.cli:cli',
        ],
    }
)
