from setuptools import setup, find_packages

setup(
    name="clean_folder",
    version="0.1",
    author="Vladislav",
    entry_points={
        'console_scripts': ['clean=clean_folder.clean:main'],
    },
    packages=find_packages(),
    description="Clean folder script",
)
