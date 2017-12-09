# templ `example-notes` branch

This orphan branch provides an example of a notekeeping system put together with the templ system.
I use this system to organize:
* draft blog articles,
* class notes,
* notes on meetings,
* summaries of papers I read, and
* notes from talks I go to.

## Taking Notes

I do this to make a new blog entry draft.
```
atom $(templ blog)
```

I do this to make new class notes.
```
atom $(templ class)
```

I do this to take notes on a meeting.
```
atom $(templ meet)
```

I do this to write a little summary of a paper I just read.
```
atom $(templ paper)
```

I do this to open a note-taking sheet for a talk or workshop I'm at.
```
atom $(templ talk)
```

## Compiling Notes to PDF, HTML, and Microsoft Word

`Makefile` uses pandoc to compile specific notes to a PDF, HTML, or Microsoft Word document document when I want to.

For example, this is how I compile the blog article `blog/12-2017-communication-workshop.md` to a HTML document.
```
make out/blog/12-2017-communication-workshop.html
```
This is especially handy because our lab blogs through Wordpress.
This way, I can write in Markdown in my favorite text editor then just paste the HTML into Wordpress when I am done.

If I want a Microsoft Word document to upload to Google Docs for feedback, I do this.
```
make out/blog/12-2017-communication-workshop.doc
```

Making a PDF copy of my article is as easy as this.
```
make out/blog/12-2017-communication-workshop.pdf
```

The Makefile is designed so that similar actions will work on all of your Markdown (`.md`) documents.
