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
    version = "0.6.1",
    description = "A templating tool for maintaining a journal or notes.",
    long_description = long_descr,
    author = "Matthew Andres Moreno",
    package_data = {
        # if any package contains *.yaml fiels, include them:
        '': ['templates/*.yaml'],
    },
    author_email = "matthew.andres.moreno@gmail.com",
    url = "https://github.com/mmore500/templ",
    )
