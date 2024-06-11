(repo)=
# Repository

Topics related to a project's Git repository.


(repo-remote)=
## Put a bare repository on a server

Synchronizing all your work with a Git repository on a server has several advantage:

- You don't need to backup your repository
- You can more easily work on your project on different platforms (laptop, desktop, ...)
- You can collaborate with colleagues

:::{margin} GTD
GiHub is not Git and Git is not GitHub. GitHub is a popular way for managing Git repositories and provides
many useful tools for collaborating on a project. GitLab does something similar in a slightly different way.
More options exist, like Codeberg, Gitea and Forgejo, and it is also possible to setup a Git server yourself.
:::


(repo-organize)=
## Organize repositories by platform and grouping construct

Before you know it, you will have multiple Git repositories cloned on your computer. You need to decide on a
way to organize these. One option is to organize them first by platform (like `github` in case of GitHub), and
then by grouping construct as used on the platform (like the organization on GitHub). This way, repositories
with the same name but in different organizations, like a fork for example, will end up in a unique location
in the file system.

Example file system tree of directories with Git repositories from different platforms:

```
project/
    github/
        own_organization/
            cool_soft/
        team_organization/
            cool_soft/
    gitlab/
        university/
            faculty/
                department/
                    cool_package/
```

See also:

- [](#repo-fork-contribute)
- [](#deps-separate-source-build)


(repo-pre-commit)=
## Use pre-commit

Pre-commit helps to prevent that your repository becomes a mess. For example, over time you may want to switch
how you format code, or receive contributions from others that use a different style. All people contributing
to a repository should adhere to the style of the surrounding code, but deviations may creep in, slowly
turning the repository into a mess. Some people refer to this as an "old" repository. Old repositories are not
nice to contribute to. Other reasons for a repository to become old is the accidental inclusion of generated
files, large files, and files with different line endings, but also spelling errors in comments, error
messages, and documentation.

There are tools that you can run to check whether files adhere to certain rules, like the code's formatting
style, for example. Some of these tools even fix any deviations from the "correct" style. Running these tools
each time you have made a change quickly becomes a hassle.

Pre-commit helps you to automatically run tools that check and fix changes made to your repository every time
you want to commit these changes. On the website you can find a repository of easy to use hooks which you can
refer to from the Pre-commit configuration file.

See also:

- [pre-commit.com](https://pre-commit.com)
- [](#deps-separate-source-build)
- [](#py-black)
- [](#py-mypy)


(repo-small-changes)=
## Make small changes

TODO

See also:

- [](#repo-issue-per-change)


(repo-issue-per-change)=
## Create an issue per change

TODO

See also:

- [](#repo-name-branch)


(repo-name-branch)=
## Name branch after issue ID

A branch requires a name. To keep things simple and not have to think about names all the time, just name the
branch after the issue ID. When creating an issue, it is assigned an ID. On GitHub you can find it in the
interface and in the address bar.

```bash
git checkout -b gh123
```

An additional benefit of using issue IDs in a branch name is that it becomes easier to interpret the log of
commit messages. To understand why a branch was merged, just lookup the issue with the corresponding ID.

- [](#repo-merge-bubbles)


(repo-changes-in-branch)=
## Make changes in a branch

Whenever you want to make a change to a repository, put the updates in a separate branch. This will make it
easier for you to to work on multiple issues "at the same time", and to collaborate with others.

See also:

- [](#repo-name-branch)
- [](#repo-issue-per-change)
- [](#repo-small-changes)


(repo-merge-bubbles)=
## Use merge bubbles when merging branches

TODO


(repo-fork-contribute)=
## Fork, then contribute

If you want to contribute to someone else's repository, to which you do not have write permissions, you must
fork the project first. You can then make changes within a branch of the copy of the original repository. Once
finished, you can submit a pull request to the original repository, based on your branch.

This process also works for your own repository, to which you do have write permissions. To keep things
simple, and to understand what people contributing to your repository have to go through, you can use this way
of contributing to a repository in all cases.

Example workflow in case of GitHub:

1. Find repository in its organization and fork it
1. Find repository in own organization and clone it
1. Create a branch for your updates

   ```bash
   git checkout -b gh123
   ```
1. Push branch to your version of the repository

   ```bash
   git push -u origin gh123
   ```

1. Submit a PR

   ```bash
   TODO
   ```

To keep your copy of the repository (AKA downstream repository) up-to-date with the repository you forked from
(AKA the upstream repository), you can use this workflow:

1. Add a remote referencing the upstream repository

   ```bash
   git remote add upstream url/to/upstream/project.git
   ```

1. If anything changed in the upstream main (or master) branch

   ```bash
   # Update your version of upstream's main branch
   git checkout main
   git pull upstream main
   git push

   # Rebase your work on updated main branch
   git checkout gh123
   git rebase main
   git push
   ```


See also:

- https://docs.github.com/en/pull-requests
- [](#repo-organize)
- [](#repo-name-branch)
