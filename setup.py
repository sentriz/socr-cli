from setuptools import setup


setup(
    name="socr",
    version="0.0",
    author="Senan Kelly",
    author_email="senan@senan.xyz",
    packages=[
        'socr',
    ],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
          'socr = socr.cli:cli',
        ],
    }
)
