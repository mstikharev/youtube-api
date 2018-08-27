from setuptools import setup, find_packages

setup(
    name='stikpro-youtube-api',
    version='0.1',
    description='Youtube API lib for stikpro',
    url='https://github.com/fn12gl34/youtube-api',
    author='Dmitry Kuzmin',
    author_email='dmitrykzmn@hotmail.com',
    packages=find_packages(),
    install_requires=[
        'apiclient',
        'google-api-python-client'
    ],
)
