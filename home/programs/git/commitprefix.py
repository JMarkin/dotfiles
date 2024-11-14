#!/usr/bin/env python
# set ft=python
import sys, re
from subprocess import check_output

commit_msg_filepath = sys.argv[1]

branch = check_output(["git", "symbolic-ref", "--short", "HEAD"]).strip().decode()

prefixes = "(feature|feat|fix|hotfix|refactor|docs|temp)(/|-)"

issue_ = re.compile(rf"{prefixes}(\w+-\d+).*")
semantic_ = re.compile(rf"{prefixes}(\w+)")


def read_write(file, prefix):
    with open(file, "r+") as fh:
        commit_msg = fh.read()
        fh.seek(0, 0)
        fh.write(f"{prefix}{commit_msg}")


if matched := re.match(issue_, branch):
    issue = matched.group(3)
    read_write(commit_msg_filepath, f"{issue}: ")
elif matched := re.match(semantic_, branch):
    issue = matched.group(3)
    semantic_name = matched.group(1)
    read_write(commit_msg_filepath, f"{semantic_name}({issue}): ")
