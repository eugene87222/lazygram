from setuptools import setup, find_packages

setup(
    name='lazygram',
    version='1.0',
    description='A wrapper of aiogram because I\'m lazy.',
    long_description='A wrapper of aiogram because I\'m lazy.',
    author='Eugene Yang',
    author_email='eugene87222@gmail.com',
    url='https://github.com/eugene87222/lazygram',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[
        'aiogram==3.6.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
