from setuptools import setup

setup(
    name='stikpro-youtube-api',
    version='0.1',
    description='Youtube API lib for stikpro',
    url='https://github.com/fn12gl34/youtube-api',
    author='Dmitry Kuzmin',
    author_email='dmitrykzmn@hotmail.com',
    packages=['lib'],
    install_requires=[
        'apiclient',
        'google-api-python-client'
    ],
)
