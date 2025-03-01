from setuptools import setup, find_packages

setup(
    name="bg_remove",  # Library name
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "rembg",
        "pillow"
    ],

)
