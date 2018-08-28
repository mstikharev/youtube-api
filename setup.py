from setuptools import setup

setup(
    name='stikpro-youtube-api',
    version='1.0',
    url='https://github.com/fn12gl34/youtube-api',
    author='Dmitry Kuzmin',
    author_email='dmitrykzmn@hotmail.com',
    py_modules=['stikpro_yt_api'],
    install_requires=[
        'apiclient',
        'google-api-python-client'
    ]
)
