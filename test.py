import main
import unittest

class test_raw_data ():
    raw_data={'sha': 'a725a0c65f81ef8cc21331bb9846f0c0752d7e23', 'node_id': 'MDY6Q29tbWl0MjI4MjkyMzcwOmE3MjVhMGM2NWY4MWVmOGNjMjEzMzFiYjk4NDZmMGMwNzUyZDdlMjM=', 'commit': {'author': {'name': 'Bob Sullivan', 'email': 'bsullivan@singledigits.com', 'date': '2019-12-18T13:16:49Z'}, 'committer': {'name': 'Bob Sullivan', 'email': 'bsullivan@singledigits.com', 'date': '2019-12-18T13:16:49Z'}, 'message': 'Update test.txt', 'tree': {'sha': 'b6834f6fd4b4ea965a01815b10909bcc7318c567', 'url': 'https://api.github.com/repos/***/DockerLearning/git/trees/b6834f6fd4b4ea965a01815b10909bcc7318c567'}, 'url': 'https://api.github.com/repos/***/DockerLearning/git/commits/a725a0c65f81ef8cc21331bb9846f0c0752d7e23', 'comment_count': 0, 'verification': {'verified': False, 'reason': 'unsigned', 'signature': None, 'payload': None}}, 'url': 'https://api.github.com/repos/***/DockerLearning/commits/a725a0c65f81ef8cc21331bb9846f0c0752d7e23', 'html_url': 'https://github.com/***/DockerLearning/commit/a725a0c65f81ef8cc21331bb9846f0c0752d7e23', 'comments_url': 'https://api.github.com/repos/***/DockerLearning/commits/a725a0c65f81ef8cc21331bb9846f0c0752d7e23/comments', 'author': {'login': '***', 'id': '********', 'node_id': 'MDQ6VXNlcjU2NDA0ODg5', 'avatar_url': 'https://avatars0.githubusercontent.com/u/56404889?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/***', 'html_url': 'https://github.com/***', 'followers_url': 'https://api.github.com/users/***/followers', 'following_url': 'https://api.github.com/users/***/following{/other_user}', 'gists_url': 'https://api.github.com/users/***/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/***/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/***/subscriptions', 'organizations_url': 'https://api.github.com/users/***/orgs', 'repos_url': 'https://api.github.com/users/***/repos', 'events_url': 'https://api.github.com/users/***/events{/privacy}', 'received_events_url': 'https://api.github.com/users/***/received_events', 'type': 'User', 'site_admin': False}, 'committer': {'login': '***', 'id': '**********', 'node_id': 'MDQ6VXNlcjU2NDA0ODg5', 'avatar_url': 'https://avatars0.githubusercontent.com/u/56404889?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/***', 'html_url': 'https://github.com/***', 'followers_url': 'https://api.github.com/users/***/followers', 'following_url': 'https://api.github.com/users/***/following{/other_user}', 'gists_url': 'https://api.github.com/users/***/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/***/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/***/subscriptions', 'organizations_url': 'https://api.github.com/users/***/orgs', 'repos_url': 'https://api.github.com/users/***/repos', 'events_url': 'https://api.github.com/users/***/events{/privacy}', 'received_events_url': 'https://api.github.com/users/***/received_events', 'type': 'User', 'site_admin': False}, 'parents': [{'sha': 'c3d28d2fc8937b3b5bc70234f48b917bc64f35c2', 'url': 'https://api.github.com/repos/***/DockerLearning/commits/c3d28d2fc8937b3b5bc70234f48b917bc64f35c2', 'html_url': 'https://github.com/***/DockerLearning/commit/c3d28d2fc8937b3b5bc70234f48b917bc64f35c2'}], 'stats': {'total': 2, 'additions': 1, 'deletions': 1}, 'files': [{'sha': '9366d2c51efddddde160b95cd3b2e0b1fb1c029b', 'filename': 'build/test.txt', 'status': 'modified', 'additions': 1, 'deletions': 1, 'changes': 2, 'blob_url': 'https://github.com/***/DockerLearning/blob/a725a0c65f81ef8cc21331bb9846f0c0752d7e23/build/test.txt', 'raw_url': 'https://github.com/***/DockerLearning/raw/a725a0c65f81ef8cc21331bb9846f0c0752d7e23/build/test.txt', 'contents_url': 'https://api.github.com/repos/***/DockerLearning/contents/build/test.txt?ref=a725a0c65f81ef8cc21331bb9846f0c0752d7e23', 'patch': '@@ -1 +1 @@\n-w\n\\ No newline at end of file\n+ws\n\\ No newline at end of file'}]}


class test_changes ():
    commit = test_raw_data()

class pull_request_test():
    def __init__(self):
        self.file1 = file_test("test1/test1.txt")
        self.file2 = file_test("test2/test2.txt")

    def get_files(self):
        return {self.file1, self.file2}


class file_test():
    def __init__(self, filename):
        self.filename = filename


class TestPullRequest(unittest.TestCase):

    def pr_test(self):
        self.assertEqual(main.return_file_paths_that_have_changed_files(pull_request_test()), ['test1/', 'test2/'])


if __name__ == '__main__':
    unittest.main()