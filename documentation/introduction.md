# Introduction

In this document we provide guidelines for setting up and maintaining a model development project.  It is
targeted at model developers who are not also experienced software developers, but for example domain experts
who develop models part-time.

We assume that you use Git to manage versions of your model's source files, and that you use Python as the
programming language for implementing the model. In this document you will not find information about why to
use Git or Python, nor is it an introduction to them. You probably already know at least the basics, maybe
because you followed a course.

Here, you will find information that is a bit harder to find, for example because it is hidden in books you
may never read because they are about the practice of software development in general, or because it requires
more experience than you may have.

:::{margin} GTD
You may have heard of the book called [Getting Things
Done](https://en.wikipedia.org/wiki/Getting_Things_Done). Among other things, the author describes how to
*effectively* use things like mailboxes and a file cabinet (digital or analog). The goal is to become more
productive and less stressful, using things you already use, but in a better way. We hope this document will
have the same result, but in the domain of model development using Python.
:::

To illustrate the gap we are trying to fill, assume asking 10 domain experts to implement a certain model and
provide you with the end result. It is very likely that you will end up with 10 different sets of files with
different contents. The layout of the repositories will be different, as will the names of the files, the design
of the code, the layout of the code, the naming conventions used in the code, etc. Why is this the case?
Because each model developer individually makes decisions about these matters while implementing their model,
based on their preference, experience and the set of tools they use. The problem with this is that it makes it
harder than necessary to collaborate with each other. Using similar conventions and coding practices make it
easier for us all to understand each other's code. For some of the conventions and practices good guidelines
exist. We think it is a good thing when model developers know about these, hence this document.

:::{note}
You may not agree with every guideline we provide, and maybe for good reasons. Use the ones you think are
useful.
:::

We have grouped the guidelines. The order in which we discuss these groups mostly corresponds with the order
in which they are useful to know when starting a new model development project: setup a repository, handle
dependencies, add Python code. There is no need to read things in order, so you can browse to any topic that
interests you. We have added links between related topics.

This document will change over time, as we improve existing guidelines and include new ones. We invite you to
help with this by suggesting better ways to describe guidelines and suggesting new ones, for example. In case
you are really inspired then please fork the repository, make improvements, and submit a pull request
([](#repo-fork-contribute)).
