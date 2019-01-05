# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


from setuptools import setup



with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "templ",
    packages = ["templ"],
    entry_points = {
        "console_scripts": ['templ = templ.templ:main']
        },
    version = "0.9.0",
    description = "A templating tool for maintaining a journal or notes.",
    long_description = long_descr,
    author = "Matthew Andres Moreno",
    package_data = {
        '': ['templates/*.yaml'],
    },
    install_requires=[
          'pyyaml',
     ],
    author_email = "m.more500@gmail.com",
    url = "https://github.com/mmore500/templ",
    )
