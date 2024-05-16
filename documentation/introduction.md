# Introduction
In this document we provide tips and tricks for setting up and maintaining a model development project.
It is targeted at model developers who are not also experienced software developers, for example domain
experts who develop models part-time.

We assume that you use Git to manage versions of your model's source files, and that you use Python as the
programming language for implementing the model. In this document you will not find information about why to
use Git or Python, and how they work. You probably already know that, maybe because you followed a course.

In this document you will find information that is a bit harder to find, for example because it is hidden in
books you may never read because they are about the practice of software development in general, or because
it requires more experience than you may have.

To illustrate the gap we are trying to fill, assume asking 10 domain experts to implement a certain model and
provide you with the end result. It is very likely that you will end up with 10 different sets of files with
different contents. The layout of the repository will be different, as will the names of the files, the
design of the code, the layout of the code, the naming conventions used in the code, etc. Why is this the
case? Because each model developer individually makes decisions about these matters while implementing their
model, based on their preference and experience. The problem with this is that it makes it harder than
necessary to collaborate with each other. Good conventions and good coding practices make it easier for us all
to understand each other's code. For some of the conventions and practices good guidelines exist. We think it
would be a good thing if model developers know about these conventions and good practices, and that is the gap
we are trying to fill with this document.

Apart from mentioning known conventions and practices we will also provide tips and trick we think are useful
to know. With everything we describe you may disagree, so pick whatever you think is useful.

The order in which we discuss topics mostly corresponds with the things you need to know when starting a new
model development project: setup a repository, handle dependencies, add Python code. There is no need to read
things in order, so you can browse to any topic that interests you. We try hard to provide
links between related topics.

This document will grow over time, as we include more topics. We invite you to suggest topics
for inclusion as well. In case you are really inspired please fork the repository, make
improvements, and submit a pull request.

