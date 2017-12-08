# templ

A script to initialize journal entries using a templating system.
File content and file path are both constructed from a template that:
* programmatically auto-populates certain fields like `cur-day` or `cur-month`, and
* prompts the user for values for other fields like `speaker-last` or `title`.
(The fields that the system will populate for an entry type are defined within that entry type's template file.)
Multiple entry types are supported.
Entry types are defined using YAML files.
Existing entry types can be modified and additional entry types can be defined by modifying or adding YAML templates to `templ/templates`.

## Usage
Basic usage is as follows.
```
templ [entry type]
```
If an entry file does not already exist, an appropriate templated file is initialized.

The path to the entry file is passed to `STDOUT`, regardless, allowing for fancy Bash tricks.

Open a template-initialized entry file or an existing entry file with your favorite text editor from the command line!
Remove the entry file.
Compile the entry file to a PDF with pandoc!
```
atom $(templ je)
rm $(templ pr)
pandoc -o out.pdf $(templ je)
```

You could also do it this way if, for some reason, you really wanted to.
Maybe you just like weird bash tricks.
```
eval "atom `templ oje`"
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

## Personalization
You can add your own templates or modify existing templates in `templ/templates`.
These templates use standard Python string formatting.
The user will be prompted at the command line to supply fields that aren't written into the `format_dict` in `templ/templ.py`.

Bonus points: fork this repo, and change the format dict to use your name instead of "Your Name Here" for the field `cur_author`.
If you think you might eventually want to put in a pull request, be sure to branch away from master before committing this change.

You will need to reinstall the package for any changes you make to take effect.
```
pip3 install ./templ --upgrade
```

## Contribute
If you come up with interesting new templates, write new auto-filled fields into `format_dict`, or make other enhancements/fixes please put in a pull request!
