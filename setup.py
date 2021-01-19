from setuptools import setup
setup(
    name='brutus',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'brutus=brutus:driver'
        ]
    }
)
