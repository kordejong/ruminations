(repo)=
# Repository

Topics related to a project's Git repository.


(repo-remote)=
## Put a bare repository on a server

Synchronizing all your work with a Git repository on a server has several advantage:

- You don't need to backup your repository
- You can more easily work on your project on different platforms (laptop, desktop, ...)
- You can collaborate with colleagues

:::{margin} GitHub vs Git
GiHub is not Git and Git is not GitHub. GitHub is a [forge](https://en.wikipedia.org/wiki/Forge_(software)).
Other forges exist as well, like Forgejo, Gitea, and GitLab. Some of these forges can also be self-hosted.
:::

See also:

- [](#repo-small-changes)


(repo-organize)=
## Organize repositories by host name and grouping construct

Before you know it, you will have multiple Git repositories cloned on your computer. You need to decide on a
way to organize these. One option is to organize them first by host name (like `github` in case of GitHub),
and then by grouping construct as used on the hosted forge (like the organization on GitHub). This way,
repositories with the same name but in different organizations, like a fork for example, will end up in a
unique location in the file system.

Example file system tree of directories with Git repositories from different forges:

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
    my_own_server/
        personal/
            snippets/
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
style, for example. Some of these tools can even automatically fix any deviations from the "correct" style.
Such tools can be very useful, but running them each time you have made a change quickly becomes a hassle.

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

Working on and finishing relatively small tasks has several advantages:

- It decreases the chance of loosing uncommitted work, due to a hardware failure for example
- It will make it easier to work on different tasks concurrently, either by yourself or by team members.
  Rebasing ongoing work on a huge commit increases the chance of merge conflicts you have to resolve.
- It will be easier to perform "code archaeology", to figure out what changed when a specific feature was
  introduced, for example
- It will give you a nice feeling of making progress

See also:

- [](#repo-remote)
- [](#repo-issue-per-change)
- [](#repo-changes-in-branch)


(repo-issue-per-change)=
## Create an issue / ticket per change

An issue is a single piece of work that will improve the code, like a new feature or a bug fix.

This has several advantages:

- It makes it easier to plan releases by associating specific issues that should be solved for each release
- It will be easier to collaborate. Focussed tasks often require a smaller set of skills, increasing the
  chance that someone wanting to contribute has these.
- It will make it easier to work on different tasks concurrently, either by yourself or by team members.

See also:

- [](#repo-small-changes)
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

A merge bubble results from merging a branch and creating a merge commit. A merge commit has two branches as a
parent: the branch merged and the branch merged into. In general these are a topic branch and the main branch,
respectively.

Merge bubbles make it convenient to visually inspect which commits are part of a branch, for example using
this command:

```bash
git log --oneline --decorate --graph
* 3ada53d Update deploy.yml
*   b444544 Merge pull request #1 from computationalgeography/upstream/main
|\
| * cbe713b Add deploy workflow
| * a01095e WIP
| * b422ffb Update documentation
| * dba8cd2 WIP
| * 0f84642 WIP
| * fb9b4bd WIP
| * 484ace3 Setup project
|/
* 9ac4878 Initial commit
```

Here is an example of merging a topic branch and creating a merge bubble. The relevant option is `--no-ff`.

```bash
git checkout main
git merge --no-ff gh123
git push
git branch -d gh123
```


(repo-fork-contribute)=
## Fork, then contribute

If you want to contribute to someone else's repository, to which you do not have write permissions, you must
fork the project first. You can then make changes within a branch of the copy of the original repository. Once
finished, you can submit a pull request to the original repository, based on your branch.

This process also works for your own repository, to which you actually do have write permissions. To keep
things simple, and to understand what people contributing to your repository have to go through, you can use
this way of contributing to a repository in all cases.

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
   git pull --rebase upstream main
   git push

   # Rebase your work on updated main branch
   git checkout gh123
   git rebase main
   git push
   ```

:::{warning}
Except from merging updates from upstream's main branch, don't commit other updates to your version of
upstream's main branch. You want to keep both main branches identical.
:::

See also:

- https://docs.github.com/en/pull-requests
- [](#repo-organize)
- [](#repo-name-branch)


(repo-clean-repository)=
## Keep the repository clean

A clean repository in a repository that is easy to inspect. Especially when working on a repository with
multiple people, it is easy for the repository to become a mess. A messy repository is one that is difficult
to understand. It is hard to figure out who did what and why. Also, a messy repository is hard to work with.
Git may throw all kinds of error messages at you that may be hard to understand and fix. Spending time on
fixing messy repositories is a waste and can be prevented by:

- Understand how a clean repository looks like. This determines when it is OK to push commits to a remote.
- Git workflows for keeping a repository clean. This helps staying productive with Git.

Git is a very flexible and powerful tool, but without some guidelines it is easy to mess things up. Here we
describe a Git workflow that is simple to use and keeps your repository clean. Many projects use a similar
workflow.

1. The main branch must always be in a good state. This is the current development version of your project.
   Never commit anything into main that will break things.
   ```{mermaid}
   %%{init: {'theme': 'neutral'} }%%
   gitGraph:
       commit id:"1"
       commit id:"2"
       commit id:"3"
   ```
1. Development is always done in topic branches. The state of the code in this branch is up to the people
   working on it. Once finished and everything works, the topic branch can be merged into the main branch and
   deleted.
   ```{mermaid}
   %%{init: {'theme': 'neutral'} }%%
   gitGraph:
       commit id:"1"
       branch gh123
       checkout gh123
       commit id:"a"
       checkout main
       commit id:"2"
       commit id:"3"
       checkout gh123
       commit id:"b"
       checkout main
       merge gh123
       commit id:"4"
   ```
1. When merging a branch into the main branch, rebase it first, to prevent hard-to-solve merge conflicts and
   braided merge patterns.
   ```{mermaid}
   %%{init: {'theme': 'neutral'} }%%
   gitGraph:
       commit id:"1"
       commit id:"2"
       commit id:"3"
       branch gh123
       checkout gh123
       commit id:"a"
       commit id:"b"
       checkout main
       merge gh123
       commit id:"4"
   ```

A clean repository has a branching pattern that looks like this:

```{mermaid}
%%{init: {'theme': 'neutral'} }%%
gitGraph:
   commit id:"1"
   branch gh123
   checkout gh123
   commit id:"a"
   commit id:"b"
   checkout main
   merge gh123
   branch gh456
   checkout gh456
   commit id:"c"
   commit id:"d"
   commit id:"e"
   checkout main
   merge gh456
   branch gh789
   checkout gh789
   commit id:"f"
   checkout main
   merge gh789
   commit id:"2"
```

It is now easy to (visually) inspect the commits that have contributed to solving the various issues (`123`,
`456`, `789`). They are part of the corresponding topic branches. Each of the topic branches has contributed a
series of commits to the main branch.

Merge conflicts can mostly be prevented this way, although they still can occur. Rebasing a topic branch on an
updated main branch will merge commits from the topic branch with the new commits from the main branch. This
may result in conflicts that have to be solved. The good thing is that this can happen as part of the ongoing
work on the issue. Solving such conflicts is likely to be easier than solving conflicts when merging a ready
topic branch with an updated master branch. This is especially true when rebasing a topic branch happens
regularly. Rebasing topic branches on top of an updated main branch can happen as often as needed. Merging a
topic branch into the main branch happens only once, once the related issue is solved.

```{note}
Merging a topic branch that has been rebased on the main branch will never result in merge conflicts.
```

See also:

- [](#repo-issue-per-change)
- [](#repo-changes-in-branch)
- [](#repo-merge-bubbles)
- GitHub provides a "network graph", showing the branching pattern. Find it in your repository: Insights |
  Network. Other forges likely provide a similar feature, as does Git itself, e.g.:
  ```bash
  git log --oneline --decorate --graph
  ```
