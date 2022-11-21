from setuptools import setup
from setuptools import find_packages
import os

cwd = os.path.dirname(os.path.realpath(__file__))
file = os.path.join(cwd, 'requirements.txt')

with open(file) as f:
    dependencies = list(map(lambda x: x.replace("\n", ""), f.readlines()))


with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    # Define the library name, this is what is used along with `pip install`.
    name='trademl',

    # Define the author of the repository.
    author='Andrey Konshin, Nikita Mikhalkovich',

    # Define the Author's email, so people know who to reach out to.
    # author_email='coding.sigma@gmail.com',

    # Define the version of this library.
    # Read this as
    #   - MAJOR VERSION 0
    #   - MINOR VERSION 1
    #   - MAINTENANCE VERSION 0
    version='0.1.0',

    # Here is a small description of the library. This appears
    # when someone searches for the library on https://pypi.org/search.
    description='Library with all needed classes',

    # This will specify that the long description is MARKDOWN.
    long_description_content_type="text/markdown",

    install_requires=[dependencies, "ta-lib==0.4.19"],

    dependency_links=["https://github.com/mrjbq7/ta-lib#egg=TA-lib-0.4.19"],

    # Here are the keywords of my library.
    keywords='ANS Technologies, trademl, classes',

    # here are the packages I want "build."
    packages=['trademl'],

    # # here we specify any package data.
    # package_data={

    #     # And include any files found subdirectory of the "td" package.
    #     "td": ["app/*", "templates/*"],

    # },

    # I also have some package data, like photos and JSON files, so
    # I want to include those as well.
    include_package_data=True,

    # Here I can specify the python version necessary to run this library.
    python_requires='>=3.7',

    # Additional classifiers that give some characteristics about the package.
    # For a complete list go to https://pypi.org/classifiers/.
    classifiers=[
        'Intended Audience :: Science/Research',

        'License :: MIT License',

        'Natural Language :: English :: Russian',

        'Operating System :: OS Independent',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',

        'Topic :: Data Science :: Machine Learning',
    ]
)
