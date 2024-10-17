# Mastering Google Colab: A Comprehensive Guide

## Introduction

Google Colab is a powerful platform for Generative AI, data science, software development, and general computing tasks. It also provides a platfrom for [generating code](https://www.youtube.com/watch?v=56O6qgEWuZU) using LLM. This guide provides an overview of the Linux shell commands available in Google Colab, as well as tips for accessing a runtime terminal, transferring files between Google Drive and Colab, and more. Whether you're a seasoned user or just getting started, this guide will help you unlock the full potential of Google Colab.


Google Colab runs on a **Linux-based operating system**, specifically a variant of **Ubuntu**. As of recent updates, Colab is typically running on **Ubuntu 20.04 LTS (Focal Fossa)**, although the exact version may vary as Google periodically updates the backend infrastructure.

You can verify the OS version in your current Colab environment by running the following terminal command in a code cell:

```bash
!cat /etc/os-release
```

This will display detailed information about the Linux distribution, including the name and version of the OS. Here’s an example output:

```bash
NAME="Ubuntu"
VERSION="20.04.6 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.6 LTS"
VERSION_ID="20.04"
```

The OS also comes pre-installed with common development tools and libraries, such as Python, Jupyter, Git, and various machine learning libraries like TensorFlow and PyTorch.

## Using Shell Commands in Code Cell

In Google Colab, you have access to a wide range of Linux shell commands through the code cell. Since Colab runs on an Ubuntu-based Linux environment, most common Linux commands are available. Here are some categories and examples of commands you can use:

_**Note:**_ In order to run any of below commands, make sure to add **!** before any command in code cells for command-line operations. i.e.

```bash
!ls
```

### 1. _File Management_

- _Listing Files and Directories:_ `ls, ls -l, ls -a`
- _Changing Directories:_ `cd [directory]`
- _Copying Files:_ `cp source destination`
- _Moving/Renaming Files:_ `mv source destination`
- _Removing Files/Directories:_ `rm filename, rm -r directory`
- _Creating Directories:_ `mkdir [directory_name]`

### 2. _System Information_

- _Disk Space Usage:_ `df -h`
- _Memory Usage:_ `free -h`
- _Checking os version:_ `lsb_release -a`
- _CPU Information:_ `lscpu`
- _OS Information:_ `uname -a, lsb_release -a`
- _Check GPU:_ `nvidia-smi`

### 3. _Networking_

- _Check Network Configuration:_ `ifconfig, ip a`
- _Download Files:_ `wget [url], curl -O [url]`
- _Ping a Server:_ `ping [hostname]`

### 4. _Package Management_

- _Update Package List:_ `apt-get update`
- _Install Packages:_ `apt-get install [package_name]`
- _Remove Packages:_ `apt-get remove [package_name]`

### 5. _Text Processing_

- _Viewing File Content:_ `cat filename, less filename, more filename`
- _Searching Text in Files:_ `grep 'pattern' filename`
- _File Editing:_ `nano filename, vi filename (though minimal terminal editors are more commonly used)`

### 6. _Permissions and Ownership_

- _Change File Permissions:_ `chmod [permissions] filename`
- _Change Ownership:_ `chown [user]:[group] filename`

### 7. _Process Management_

- _List Running Processes:_ `ps aux, top, htop`
- _Kill a Process:_ `kill [PID]`

### 8. _Python and Scripting_

- _Run Python Scripts:_ `python script.py, python3 script.py`
- _Run Shell Scripts:_ `bash script.sh, sh script.sh`

### 9. _Version Control_

- _Git Commands:_ `git clone [repo], git pull, git push`

### 10. _Miscellaneous_

- _Clear the Terminal Screen:_ `clear`
- _Check Current Directory:_ `pwd`

These commands allow you to perform a wide range of tasks directly from the Colab environment, making it quite versatile for data science, software development, and general computing tasks.

## Using Runtime Terminal in Google Colab

Google Colab's free version does not provide a built-in runtime terminal. However, you can still access a runtime terminal without purchasing a paid subscription.

![Paid subscription](images/paid_subscription.PNG)

To do so, follow these steps:

1. **Install the terminal package:** !pip install colab-xterm
2. **Load the terminal extension:** %load_ext colabxterm
3. **Launch the terminal:** %xterm

   ![runtime_terminal](images/Runtime_terminal.PNG)

With this runtime terminal, you can download additional software and tools.

## Different Options to Access Terminal

You can use a terminal in Google Colab in various ways, ranging from executing basic shell commands in notebook cells to establishing a full SSH connection or even using tools like `ngrok` to access a more interactive environment. Here’s a detailed guide covering all the possible options:

### 1. **Running Terminal Commands in Code Cells**
Colab allows you to run terminal commands directly from a code cell by prefixing the command with an exclamation mark (`!`).

#### **Basic Commands**
You can run most Linux shell commands using this method:
- List files in the current directory:
  ```python
  !ls
  ```
- Check the working directory:
  ```python
  !pwd
  ```
- Install Python packages:
  ```python
  !pip install numpy
  ```
- Use `apt-get` to install system packages:
  ```python
  !apt-get install ffmpeg
  ```

#### **Multiple Commands in One Cell**
You can also run multiple commands by chaining them:
```python
!pwd && ls -la
```

### 2. **Using `%%bash` Magic for Multiple Commands**
For executing multiple shell commands in one cell, you can use the `%%bash` magic command. This creates a bash script environment where you can execute multiple commands, just like in a shell script.

Example:
```bash
%%bash
echo "Hello from bash"
ls -la
```

This is useful when you want to run several bash commands together without using `!` for each command.

### 3. **Accessing a Full Terminal via SSH**
If you need a full interactive terminal (like a bash shell), you can establish an SSH connection to your Colab environment.

Here’s how you can set it up:

#### **Step 1: Install `colab_ssh` Package**
```python
!pip install colab_ssh --upgrade
```

#### **Step 2: Set Up SSH**
You can use the following code to get SSH access to your Colab VM. You need to set up an SSH key pair and use it to connect. Here’s an example using `colab_ssh`:

```python
from colab_ssh import launch_ssh

launch_ssh("your_password", "your_public_key")
```

- Replace `"your_password"` with a password you want to set for the SSH connection.
- Replace `"your_public_key"` with your actual SSH public key (you can generate one using tools like `ssh-keygen`).

#### **Step 3: Connect via SSH**
Once you’ve launched the SSH service, you can use any terminal that supports SSH (e.g., the terminal on your local machine) to connect to the Colab instance:

```bash
ssh root@<instance_address> -p 22
```

The `<instance_address>` will be provided to you by the `colab_ssh` library after launching the SSH service.

### 4. **Exposing a Terminal with `ngrok`**
If you prefer using `ngrok` to expose your Colab terminal or want to provide remote access, you can set up `ngrok` to tunnel SSH to your local machine.

#### **Step 1: Install `ngrok`**
```python
!pip install pyngrok
```

#### **Step 2: Set Up `ngrok`**
Create a tunnel with `ngrok` to expose the Colab environment:
```python
from pyngrok import ngrok

# Start the SSH tunnel
ssh_tunnel = ngrok.connect(22, "tcp")

# Get the ngrok URL
ssh_tunnel.public_url
```

This command creates an SSH tunnel. It will provide you with a public URL for SSH access, something like `tcp://0.tcp.ngrok.io:12345`. You can use this address to connect to your Colab instance via SSH:

```bash
ssh root@0.tcp.ngrok.io -p 12345
```

To secure your SSH connection, you may need to configure SSH authentication with public/private key pairs.

### 5. **Using `tmux` or `screen` for Persistent Sessions**
When working in Colab, your session may occasionally get disconnected. To avoid losing progress, you can use terminal multiplexers like `tmux` or `screen` within the Colab shell. They allow you to keep your terminal session alive even if your Colab notebook disconnects.

#### **Installing `tmux` or `screen`**
```python
!apt-get install tmux
```

#### **Starting a `tmux` session**
```bash
!tmux
```

Once inside `tmux`, you can run your commands as usual, and even if your Colab environment disconnects, you can resume the session later by reattaching to the `tmux` session.

### 6. **Using `localtunnel` or Alternatives**
Besides `ngrok`, you can use other tunneling services like `localtunnel` to expose the terminal or web services running on your Colab instance.

#### **Step 1: Install `localtunnel`**
```python
!npm install -g localtunnel
```

#### **Step 2: Run a Localtunnel Command**
To expose port `8080` (or any other port where your service is running):
```python
!lt --port 8080
```

This will provide you with a public URL that can be used to access the terminal or any other service running on the Colab instance.

### 7. **Jupyter Terminal in Colab (Advanced)**
Google Colab doesn’t natively support a standalone terminal like Jupyter Notebooks, which has a "Terminal" tab. However, you can emulate a Jupyter environment with `Jupyter Lab` to achieve a similar terminal interface.

#### **Step 1: Install Jupyter Lab**
```python
!pip install jupyterlab
```

#### **Step 2: Launch Jupyter Lab**
```python
!nohup jupyter-lab --ip=0.0.0.0 --port=8888 --no-browser &
```

#### **Step 3: Expose Jupyter Lab Using `ngrok`**
You can use `ngrok` to expose the Jupyter Lab interface:
```python
from pyngrok import ngrok

ngrok_tunnel = ngrok.connect(8888)
ngrok_tunnel.public_url
```

Now, you can access Jupyter Lab from the provided `ngrok` URL, where you’ll have access to a full terminal interface in addition to your Colab notebooks.

### 8. **Running Background Processes**
You can also run background processes in Colab just like you would in a regular terminal by using the `&` symbol to run commands in the background:
```bash
!python my_script.py &
```

This is useful if you need to run long-running tasks while continuing to work on other things in the notebook.

### Summary of Terminal Access in Google Colab:
1. **Basic Terminal Commands in Code Cells**: Use `!` to execute individual commands.
2. **`%%bash` Magic**: Run multiple shell commands together.
3. **SSH Connection**: Use `colab_ssh` or set up SSH with `ngrok` for full terminal access.
4. **`ngrok`/Tunneling**: Expose a terminal or service using `ngrok` or similar tools.
5. **Persistent Sessions**: Use `tmux` or `screen` to maintain sessions across disconnections.
6. **Jupyter Lab with Terminal**: Install and access Jupyter Lab for a full terminal experience.

Each method has its own use case, and depending on your needs, you can use a combination of these methods for better control over the environment.






## Copying files between google drive, Colab and vice versa.

We can Copy files between Google Colab and Google Drive using terminal commands. First, you'll need to mount your Google Drive in the Colab environment. Once mounted, you can use terminal commands like cp to copy files between Colab and Google Drive.

### Step-by-Step Guide

#### 1. Mount Google Drive

You need to mount Google Drive to your Colab session. Run the following code in a Colab cell:

```python
from google.colab import drive
drive.mount('/content/drive')
```

This will prompt you to authorize access to your Google Drive account. Follow the instructions and provide the authorization code when prompted.

#### 2. Copy Files from Colab to Google Drive

To copy all files from a directory in Colab to a directory in Google Drive, use the cp command. Here's an example:

```bash
# Replace 'source_directory' with the directory in Colab you want to copy
# Replace 'target_directory' with the target directory in your Google Drive
!cp -r /content/source_directory /content/drive/MyDrive/target_directory
```

- /content/source_directory is the path to the directory in Colab you want to copy.
- /content/drive/MyDrive/target_directory is the path to your target directory in Google Drive.

#### 3. Retrieve Files from Google Drive to Colab

To copy files from Google Drive back to Colab, use a similar cp command:

```bash
# Replace 'source_directory' with the directory in Google Drive
# Replace 'target_directory' with the target directory in Colab
!cp -r /content/drive/MyDrive/source_directory /content/target_directory
```

- /content/drive/MyDrive/source_directory is the path to the directory in Google Drive you want to copy.
- /content/target_directory is the path to the target directory in Colab.

These commands will allow you to easily copy and retrieve files between Colab and Google Drive using the terminal.

# Conclusion

In this guide, we've covered the basics of using shell commands in Google Colab, accessing a runtime terminal, and transferring files between Google Drive and Colab. Here's a quick summary of the key takeaways:

- You can use a wide range of Linux shell commands in Google Colab's code cells by prefixing them with !.
- You can access a runtime terminal in Google Colab's free version by installing the colab-xterm package.
- You can transfer files between Google Colab and Google Drive using terminal commands like cp and mv.

With these skills, you'll be well-equipped to tackle a wide range of tasks in Google Colab. For further learning, we recommend exploring the official Google Colab documentation and seeking out additional resources on Linux shell commands and terminal usage.

### Additional Resources

- [Google Colab Documentation](https://colab.research.google.com/notebooks/intro.ipynb)
- [Linux Shell Commands Tutorial](https://www.tutorialspoint.com/unix/index.htm)
- [Terminal Usage Guide:](https://www.gnu.org/software/bash/manual/bash.html)
