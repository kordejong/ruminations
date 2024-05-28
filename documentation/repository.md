# Repository


(repo-organize)=
## Organize repositories by platform and grouping construct

Before you know it, you will have many Git repositories stored on your computer. You need to decide on a way
to organize these. One option is to organize them first by platform (like `github` in case of GitHub), and
then by grouping construct as used on the platform (like the organization on GitHub). Repositories with the
same name but in different organizations, for example, will end up in a unique location in the filesystem.

It is easy to end up with repositories with the same name in the filesystem. This happens every time you fork
and then clone a repository ([](#repo-fork-contribute)).

Example filesystem tree of directories with Git repositories form different platforms:

```
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


(repo-fork-contribute)=
## Fork, then contribute

Example workflow in case of GitHub:

1. Find repository in its organization and fork it
1. Find repository in own organization and clone it ([](#repo-organize))
1. ...
