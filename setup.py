from setuptools import setup, find_packages

setup(
        name='srw',
        author='Simon Walker',
        author_email='s.walker.2@warwick.ac.uk',
        version='0.0.1',
        packages=find_packages(),
        install_requires=[
            'numpy',
            'astropy',
            'matplotlib',
            'six',
            ],
        entry_points={
            'console_scripts': [
                'find_object.py = srw.find_object:main',
                ],
            },
        )

