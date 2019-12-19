import sys
import os
from github import Github
import json
import subprocess

# Import from enviroment variables.
github_token = os.environ['INPUT_GITHUB_TOKEN']
#dockerhub_repo = os.environ['INPUT_DOCKERHUB_REPO']
docker_username = os.environ['INPUT_DOCKER_USERNAME']
docker_password = os.environ['INPUT_DOCKER_PASSWORD']
github_repo = os.environ['GITHUB_REPOSITORY']
event_path = os.environ['GITHUB_EVENT_PATH']
github_ref = os.environ['GITHUB_REF']

print(github_ref)

# Returns a list of directory paths that have Dockerfiles
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

# Returns a list of file paths and sub paths that have file changes.  Old could only pull last commit file changes, might use for on: push event
#def return_file_paths_that_have_changed_files(branch):
#    results=[]
#    files_changed = branch.commit.raw_data
#    print(files_changed)
#    if 'files' in files_changed:
#        for current_file in files_changed['files']:
#            current_filename = current_file['filename']
#            #print("FILENAME:")
#            #print(current_filename)
#            current_path_array=os.path.split(current_filename)[0].split('/')
#            recursive_path = '/'
#            for directory in current_path_array:
#                recursive_path=recursive_path + directory + '/'
#                if not recursive_path in results:
#                    results.append(recursive_path)
#    return results

# Returns a list of file paths and sub paths that have file changes
def return_file_paths_that_have_changed_files(pull_request):
    results=[]
    files_changed = pull_request.get_files()
    #print(files_changed)
    for file_changed in files_changed:
            current_filename = file_changed.filename
            #print("FILENAME:")
            #print(current_filename)
            current_path_array=os.path.split(current_filename)[0].split('/')
            recursive_path = '/'
            for directory in current_path_array:
                recursive_path=recursive_path + directory + '/'
                if not recursive_path in results:
                    results.append(recursive_path)
    return results

# Build the docker file at path that is passed in
def build_docker(dockerfile_path):
    dockerfile = str(dockerfile_path) + "/Dockerfile"
    print(dockerfile)
    subprocess.call("docker login -u " + str(docker_username) + " -p " + str(docker_password), shell=True)
    subprocess.call("docker build -t rws2154/learning:python " + str(dockerfile_path), shell=True)
    subprocess.call("docker push rws2154/learning:python", shell=True)
    subprocess.call("docker logout", shell=True)

def main():
    # Create github login to get changes, need to look into if using the ENV['GITHUB_EVENT_PATH'] is better
    github = Github(github_token)
    repo = github.get_repo(github_repo)
    
    # Read in the event_path file and load to json object.  Use that to get the pull request number
    with open(event_path) as json_file:
        event_path_data = json.load(json_file)
    
    pull_request_number = event_path_data["pull_request"]["number"]
    
    # Using the pull request number, get a pull request object to pass to the paths_that_have_files_changes function
    pull_request = repo.get_pull(pull_request_number)

    
    # Called predefined functions to get list of dockerfile path locations
    # and paths and subpaths to files that have changed
    dockerfile_path_locations = return_dockerfile_locations(repo)
    paths_that_have_file_changes = return_file_paths_that_have_changed_files(pull_request)

    # Debugging only, not used otherwise.
    # print("***********************")
    # print(dockerfile_path_locations)
    # print(paths_that_have_file_changes)
    # print("***********************")

    # Build the docker file in a path or subpath that has a file change.
    for x in paths_that_have_file_changes:
        if x in dockerfile_path_locations:
            build_docker(x)

if __name__ == "__main__":
    main()