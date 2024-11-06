#!/home/kron/.nix-profile/bin/python
# set ft=python
import sys, re
from subprocess import check_output

commit_msg_filepath = sys.argv[1]

branch = check_output(["git", "symbolic-ref", "--short", "HEAD"]).strip().decode()

prefixes = "(feature|feat|fix|hotfix|refactor|docs|temp)(/|-)"

issue_ = re.compile(rf"{prefixes}(\w+-\d+).*")
semantic_ = re.compile(rf"{prefixes}(\w+)")

if matched := re.match(issue_, branch):
    issue = matched.group(3)
    with open(commit_msg_filepath, "r+") as fh:
        commit_msg = fh.read()
        fh.seek(0, 0)
        fh.write(f"{issue}: {commit_msg}")
elif matched := re.match(semantic_, branch):
    issue = matched.group(3)
    semantic_name = matched.group(1)
    with open(commit_msg_filepath, "r+") as fh:
        commit_msg = fh.read()
        fh.seek(0, 0)
        fh.write(f"{semantic_name}({issue}): {commit_msg}")
