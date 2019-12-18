#!/usr/bin/env

from setuptools import find_packages, setup

setup(
    name="django-db-storage",
    version="1.1.1",
    url="https://github.com/derekkwok/django-db-storage",
    license="BSD",
    author="Derek Kwok",
    author_email="derek.kai.chun.kwok@gmail.com",
    description="Custom Database Storage for Django",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="django metrics analytics",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
)
