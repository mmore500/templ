# templ `example-journal` branch

This orphan branch provides an example of a journal put together with the templ system.
There are two types of files in this example journal (generated from two templates).
The first is `je` ("journal entry") files, which I write for myself.
The second is `pr` ("progress report") files, which I write for my graduate school advisor every week.

To make a new progress report or journal entry (or reopen today's progress report or journal entry), I use these commands.
```
atom $(templ pr)
atom $(templ je)
```

`Makefile` uses pandoc to compile today's journal entry or progress report to a PDF.
For example, this is how I compile my progress report to `pr-out.pdf`.
```
make pr
```
(Note that this will only work for documents that were written today.)

## Decoration

I like to put inspirational quotes in the `README.md` of my journal.
Here are two.

> All of us take pride and pleasure in the fact that we are unique, but I'm afraid that when all is said and done the police are right: it all comes down to fingerprints.

David Sedaris

> My son is taking a course in philosophy, and last night we were looking at something by Spinoza and there was the most childish reasoning!
There was all these attributes and Substances, all this meaningless chewing around, and we started to laugh.
Now how could we do that?
Here's this great Dutch philosopher, and we're laughing at him.
It's because there's no excuse for it!
In the same period, there was Newton, there was Harvey studying the circulation of the blood, there were people with methods of analysis by which progress was being made!
You can take every one of Spinoza's propositions, and take the contrary propositions, and look and the world and you can't tell which is right.

Richard Feynman
