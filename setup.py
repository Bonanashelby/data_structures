"""creating python distribution package setup.py"""
from setuptools import setup

setup(
    name="trigrams",
    description="A Python implementation of a trigrams Function.",
    version=0.1,
    author="Lynn Chen & Kurt Maurer",
    author_email="",
    license='MIT',
    py_modules=['trigrams'],
    package_dir={'': 'src'},
    extras_require={'test': ['pytest', 'pytest-watch']},
    entry_points={
        'console_scripts': [
            "trigrams = trigrams:main"
        ]
    }
)
