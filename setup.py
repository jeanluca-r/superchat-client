# setup.py
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="superchat-client",  # Your package name (must be unique on PyPI)
    version="0.1.0",  # Start with an initial version
    author="Jean-Luca Röder",
    author_email="luca@crator.de",
    description="A Python client for the Superchat API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeanluca-r/superchat-client",  # URL to your project
    packages=setuptools.find_packages(),  # Automatically find packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change if necessary
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",  # list your dependencies
    ],
)
