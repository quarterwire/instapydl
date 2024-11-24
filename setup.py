from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

version = {}
with open(os.path.join(_here, 'instagram_dl', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name="instapydl",
    version=version["__version__"],
    description="A Python package to download Instagram Reels and scrape metadata.", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Quarterwire",
    author_email="quarterwire@outlook.com",
    url="https://github.com/quarterwire/instapydl", 
    license="MIT",
    packages=["instapydl"],
    include_package_data=True,
    install_requires=[ 
        "httpx>=0.23.0"
    ],
    python_requires=">=3.8", 
    classifiers=[
        "Development Status :: 5 - Production/Stable", 
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules", 
    ],
    keywords="instagram reels downloader scrape metadata",
)