# templ

A script to initialize journal entries using a templating system.
File content and file path are both constructed from a template that:
* programmatically auto-populates certain fields like `cur-day` or `cur-month`, and
* prompts the user for values for other fields like `speaker-last` or `title`.

(The fields that the system will populate for an entry type are defined within that entry type's template file.)
Multiple entry types are supported.
Entry types are defined using YAML files.
Existing entry types can be modified and additional entry types can be defined by modifying or adding YAML templates to `templ/templates`.

Take a look at an example journal made with templ [here](https://github.com/mmore500/templ/tree/example-journal).

Take a look at an example note-taking system made with templ [here](https://github.com/mmore500/templ/tree/example-notes).

You can read more about why I designed templ and how templ works internally [here](https://mmore500.github.io/2018/01/21/my-record-keeping-setup.html).

## Installation
You will need a python package manager to install this package.
I use pip.
```
git clone https://github.com/mmore500/templ.git
pip3 install ./templ
```

## Usage
Basic usage is as follows.
```
templ [entry type]
```
If an entry file does not already exist, an appropriate templated file is initialized.

The path to the entry file is passed to `STDOUT`, regardless, allowing for fancy Bash tricks.

Open a template-initialized entry file or an existing entry file with your favorite text editor from the command line!
For example, if I did this on January 1, 1970
```
atom $(templ je)
```
I would open a new atom tab pointed at `1970/1/1-je.md` initialized with
```
## todo

## done

## misc
```
ready for me to write down my thoughts for the day.

Templates can dynamically populate both the path and the text file generated with content generated automatically or requested from the user.
For example, when I was at a seminar on September 29th, 2017, and did this (answering some command line prompts generated by templ)
```
atom $(templ talk)
speaker-last > Wiser
keyword > conceptions-randomness
talk-title > Student conceptions about randomness and mutation
speaker-first > Michael
location > BEACON Seminar
```
I got a new atom tab pointed at `talk/Wiser-conceptions-randomness-2017-09-29.md` initialized with
```
# Student conceptions about randomness and mutation

Michael Wiser
09-29-2017
BEACON Seminar

## synopsis

## misc

```
ready for me to take notes on all of the crazy things undergraduates think about randomness.

Want to add an image to your journal?
Great!
Say you're working on your journal entry.

`journal/2018/01/21-je.md`:

~~~
## todo
* nothing

## done
* drinks on the beach

## notes
I wrote this content.
I'm using my favorite text editor so I'm happy and stuff.

:) :) :) :) :) :)

Okay, time to put an image in.

~~~

Bring back up your terminal.

~~~
mkdir $(templ jd)
mv doge.jpg $(templ jd)
templ ji
filename > doge.jpg
~~~

Now we have our image situated at `journal/2018/01/21-img/doge.jpg`.
When you switch back to your open file `journal/2018/01/21-je.md`, you'll find it with the following addition.

~~~
## todo
* nothing

## done
* drinks on the beach

## notes
I wrote this content.
I'm using my favorite text editor so I'm happy and stuff.

:) :) :) :) :) :)

Okay, time to put an image in.

![](21-img/doge.jpg)

~~~

You can keep typing.

~~~
## todo
* nothing

## done
* drinks on the beach

## notes
I wrote this content.
I'm using my favorite text editor so I'm happy and stuff.

:) :) :) :) :) :)

Okay, time to put an image in.

![](21-img/doge.jpg)

Wow, much amaze.

~~~

Here's the final rendered result.

> ## todo
> * nothing
>
> ## done
> * drinks on the beach
>
> ## notes
> I wrote this content.
> I'm using my favorite text editor so I'm happy and stuff.
>
>  :) :) :) :) :) :)
>
> Okay, time to put an image in.
>
> ![](http://devosoft.org/wp-content/uploads/2018/01/doge.jpg)
>
>  Wow, much amaze.

You can do other cool things with fancy bash tricks.
Remove the entry file.
Compile the entry file to a PDF with pandoc.
Put the entry under version control.
Remember, if the templated path already exists, no changes are made to the file living there when templ is called.
```
rm $(templ pr)
pandoc -o out.pdf $(templ je)
git add $(templ pr)
```

You could also do it this way if, for some reason, you really wanted to.
Maybe you just like weird bash tricks.
```
eval "atom `templ oje`"
```

This package is designed to facilitate keeping a tidy [journal](https://github.com/mmore500/templ/tree/example-journal) or [notebook](https://github.com/mmore500/templ/tree/example-journal) in a Git repository.
A complete workflow might look like this.
```
atom $(templ je)
git add $(templ je)
git commit
git push origin master
```
This way, you can easily review HTML renderings of your markdown notes on Github!

## Personalization
You can add your own templates or modify existing templates in `templ/templates`.
These templates use standard Python string formatting.
The user will be prompted at the command line to supply fields that aren't written into the `format_dict` in `templ/templ.py`.
For example, here is a reproduction of the template file `templ/templates/talk.yaml` that produced the example talk notes above.
```
# journal entry for notes on a talk
filename: "talk/{speaker-last}-{keyword}-{cur-year}-{cur-month:02d}-{cur-day:02d}.md"
template: |
          # {talk-title}

          {speaker-first} {speaker-last}
          {cur-month:02d}-{cur-day:02d}-{cur-year}
          {location}

          ## synopsis

          ## misc

```
Note the integer formatting employed (`{cur-day:02d}` and `{cur-day:02d}`)  that prepends one digit months and days with a zero.
Note also that the base filename of the template file determines the argument that should be provided to use the template.
For example, this template filename is `talk.yaml` so it is accessed via `templ talk`.
So if you wanted to make a template for your trainspotting notes, you would just add a file `templ/templates/train.yaml` and access it via `templ train`.

For bonus points, fork this repo, and change the format dict to use your name instead of "Your Name Here" for the field `cur-author`, your email instead of "Your Email Here" for the field `cur-author-email`, etc.
If you think you might eventually want to put in a pull request, be sure to branch away from master before committing this change.

**Important:** You will need to reinstall the package for any changes you make to take effect.
```
pip3 install ./templ --upgrade
```

## Contribute
If you come up with interesting new templates, write new auto-filled fields into `format_dict`, or make other enhancements/fixes please put in a pull request!
