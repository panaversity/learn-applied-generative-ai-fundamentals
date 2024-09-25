# Build a Book Generator AI Agent

Build a AI Agent that generates a book. The book will be hosted and pushed on Github. The directories in the repo will represent chapters, topics, and subtopics. The markdown files will contain the generated content. 

The author will give a title and description of the book to the AI Agent. The AI Agent will first generate a Table of Content and get it approved from the author. Once the chapters and topics are approved the agent will then generate the content in markdown format. Which will then be approved by the author. 

Note 1: You are free to use any LLM APIs you want.

Note 2: 

Using PyGithub is an efficient way to programmatically push content to GitHub repositories directly from memory in Python. It leverages GitHub’s REST API to perform operations without the need for local repository management.

pygit2 is another alternative you can consider for interacting with Git repositories, including pushing content to GitHub from Python. pygit2 provides Python bindings for the libgit2 library, which is a pure C implementation of Git core methods. This allows you to perform Git operations directly from Python code.