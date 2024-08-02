# Git Repository Info Sheet

This readme will help you push a repository to your online Github Repository.

### 1. Create & Activate Virtual Environment

Run `python -m venv .[venvname]`; venvname being your choice of environment name.

Run `.[venvname]\Scripts\activate`, venvname being your choice of environment name.

### 2. Configure Git

run `git config --global user.name "My name"`

run `git config --global user.email "@gmail.com"`

### 3. Initiate and ready Git

run `git init` to start git on your terminal

Make sure your `.gitignore` file is ignoring the .venvname for all the dependency files, and .env if you're using credentials etc.

run `git add .` to add your repository to the queue to add

### 4. Inital Commit and Remote URL adding

Run `git commit -m "Initial commit message"` to get your repository ready

Create a Git repository on Github.com

run `git remote add origin YOUR_REPOSITORY_URL`, with YOUR_REPOSITORY_URL as the

### 5. Push your Git Repository

For your first time, run `git push -u origin master`, where master is the channel name you're pushing to

### 6. Every subsequent submission

If you've not restarted you virtual environment:

Run `python -m venv .[venvname]`; venvname being your choice of environment name.

Run `.[venvname]\Scripts\activate`, venvname being your choice of environment name.

With your virtual environment running:

run `git init`

run `git add .`

run `git commit -m "IMessage to document changes made"`

run `git push -u origin master` to push the first time of the session.

run `git push` subsequently.

Or run `git push origin master --force` if you want to overwrite the remote repository completely.