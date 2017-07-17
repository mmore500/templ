# templ

A script to initialize journal entries using a templating system.
Multiple entry types are supported.
Entry types are defined using YAML files.
Existing entry types can be modified and dditional entry types can be defined by modifying or adding YAML templates to `templ/templates`.

## Usage
Basic usage is as follows.
```
templ [entry type]
```
Only if an entry file does not already exist, an appropriate templated file is initialized.

The path to the entry file is passed to `STDOUT`, regardless, allowing for fancy Bash tricks.

```
atom $(templ je)
eval "ls `templ oje`"
```

This package is designed to facilitate keeping a journal or notebook in a Git repository.
A complete workflow might look like this.
```
atom $(templ je)
git add $(templ je)
git commit
git push origin master
```

## Installation
You will need a python package manager to install this package.
I use PIP.
```
git clone https://github.com/mmore500/templ.git
pip3 install ./templ
```
