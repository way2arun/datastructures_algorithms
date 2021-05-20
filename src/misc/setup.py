from setuptools import setup

setup(
    name='snek',
    entry_points={
        'console_scripts': [
            'snek = snek:main',
        ],
    }
)