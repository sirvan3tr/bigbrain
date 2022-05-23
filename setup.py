from setuptools import setup

setup(
    name="bigbrain",
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Click',
        'rich',
        'meilisearch'
    ],
    entry_points='''
        [console_scripts]
        bb=main:cli
    ''',
)