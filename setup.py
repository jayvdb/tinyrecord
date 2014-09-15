from setuptools import setup, find_packages

setup(
    name='tinyrecord',
    version='0.1.1',
    packages=find_packages(),

    zip_safe=True,
    author='Eugene Eeo',
    author_email='packwolf58@gmail.com',
    description='Atomic transactions for TinyDB',
    license='MIT',
    keywords='tinydb nosql database transaction',
    url='https://github.com/eugene-eeo/tinyrecord',
)
