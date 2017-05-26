"""Create a Python distribution package setup.py."""
from setuptools import setup

setup(
    name="trigrams",
    description="A project consisting of several"
    "Python implementations of abstract data structures.",
    version=0.1,
    author="Anna and Kurt",
    license='MIT',
    py_modules=['dll', 'stack', 'linked_list'],
    package_dir={'': 'src'},
    extras_require={'test': ['pytest', 'pytest-watch']},
    entry_points={
        'console_scripts': [
        ]
    }
)
