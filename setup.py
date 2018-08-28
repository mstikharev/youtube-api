from setuptools import setup

setup(
    name='stikpro-youtube-api',
    url='https://github.com/fn12gl34/youtube-api',
    author='Dmitry Kuzmin',
    author_email='dmitrykzmn@hotmail.com',
    py_modules=['lib'],
    install_requires=[
        'apiclient',
        'google-api-python-client'
    ]
)
