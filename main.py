import sys
import os
from github import Github
import json

github_token = os.environ['GITHUB_TOKEN']

def return_dockerfile_locations(repos):
    results=[]
    contents = repos.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repos.get_contents(file_content.path))
        else:
            #print(os.path.split(file_content.path)[1])
            if os.path.split(file_content.path)[1] == "Dockerfile":
                results.append(os.path.split(file_content.path)[0])
    return results


def return_file_paths_that_have_changed_files(branch):
    results=[]
    files_changed = branch.commit.raw_data
    if 'files' in files_changed:
        for current_file in files_changed['files']:
            current_filename = current_file['filename']
            #print("FILENAME:")
            #print(current_filename)
            if not current_filename in results:
                results.append(os.path.split(current_filename)[0])
    return results


def build_docker(dockerfile_path):
    dockerfile = str(dockerfile_path) + "/Dockerfile"
    print(dockerfile)


github = Github(github_token)
repo = github.get_repo("bsullivan-sd/DockerLearning")
branch = repo.get_branch("master")
#commit = repo.get_commit(branch.commit)

dockerfile_path_locations = return_dockerfile_locations(repo)
paths_that_have_file_changes = return_file_paths_that_have_changed_files(branch)


print("***********************")
print(dockerfile_path_locations)
print(paths_that_have_file_changes)
print("***********************")

for x in paths_that_have_file_changes:
    if x in dockerfile_path_locations:
        build_docker(x)

