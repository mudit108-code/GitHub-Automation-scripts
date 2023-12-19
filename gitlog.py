import subprocess

def get_git_logs(file_path):
    try:
        # Run 'git log' command for the specified file
        command = ['git', 'log', '--follow', '--pretty=format:%h %an %s', '--', file_path]
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)

        # Split the result into individual commits
        commits = result.strip().split('\n')

        # Extract commit information
        commit_info = [commit.split(' ', 2) for commit in commits]

        return commit_info

    except subprocess.CalledProcessError as e:
        print(f"Error executing Git command: {e}")
        return None

if __name__ == '__main__':
    file_path = 'path/to/your/file.txt'  # Specify the path to your file
    logs = get_git_logs(file_path)

    if logs:
        print("Git Logs for File:")
        for commit in logs:
            print(f"Commit: {commit[0]}, Author: {commit[1]}, Message: {commit[2]}")
    else:
        print("Failed to retrieve Git logs.")
