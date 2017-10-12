from distutils.core import setup
import setuptools


setup(
    name='codepenget',
    version='',
    install_requires=[
        'requests',
        'bs4'
    ],
    packages=[
        'codepenget'
    ],
    entry_points={
        "console_scripts": [
            "codepenget = endpoints:download"
        ]
    }
)
