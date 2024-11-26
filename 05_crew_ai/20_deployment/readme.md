# CrewAI Deployment

[Deploy with CrewAI Enterprise and GitHub](https://help.crewai.com/deploying-your-crew-to-crewai)

[Deploy with Streamlit and GitHub](https://www.youtube.com/watch?v=dPPq_OS4cNw)

Deploying your CrewAI project involves several steps to ensure your AI agents are operational and accessible. CrewAI offers multiple deployment options to suit various needs, including cloud services, self-hosting, and integration with existing infrastructures. Below is a comprehensive guide to deploying your CrewAI project, along with the available deployment options.

**1. Preparing Your CrewAI Project for Deployment**

Before deploying, ensure your project is ready:

- **Codebase**: Your CrewAI project should be complete and tested locally.
- **Version Control**: Use Git to manage your code.
- **Dependencies**: List all dependencies in a `requirements.txt` file.
- **Environment Variables**: Set up necessary environment variables for API keys and configurations.

**2. Deployment Options**

CrewAI supports various deployment methods:

- **CrewAI Enterprise**: A managed service for deploying CrewAI projects.
- **Self-Hosting**: Deploy on your own infrastructure or preferred cloud service.
- **Third-Party Platforms**: Utilize platforms like Streamlit for deployment.

**3. Deploying to CrewAI Enterprise**

CrewAI Enterprise simplifies deployment with a streamlined process:

1. **Push to GitHub**: Ensure your project is in a GitHub repository.
2. **Connect GitHub to CrewAI Enterprise**: Log in to CrewAI and connect your GitHub account.
3. **Select Repository**: Choose the repository containing your CrewAI project.
4. **Set Environment Variables**: Configure necessary environment variables for LLM providers and other tools.
5. **Deploy**: Initiate deployment and monitor progress. The first deployment may take 10-15 minutes.

For detailed instructions, refer to the official guide: 

**4. Self-Hosting Your CrewAI Project**

To deploy CrewAI on your own infrastructure:

1. **Set Up Environment**: Prepare a server with the required specifications.
2. **Install Dependencies**: Install Python and necessary libraries listed in `requirements.txt`.
3. **Configure Environment Variables**: Set up environment variables for API keys and configurations.
4. **Run the Application**: Start your CrewAI application using a web server like FastAPI.
5. **Expose the Service**: Use a reverse proxy (e.g., Nginx) to expose your application to the internet.

For community discussions on self-hosting, visit: 

**5. Deploying on Third-Party Platforms (e.g., Streamlit)**

Streamlit offers a user-friendly platform for deploying Python applications:

1. **Prepare Your Project**: Ensure your CrewAI project is compatible with Streamlit.
2. **Create a Streamlit Account**: Sign up on Streamlit Cloud.
3. **Connect GitHub Repository**: Link your GitHub repository to Streamlit.
4. **Deploy**: Follow the prompts to deploy your application.





**6. Post-Deployment Considerations**

After deployment:

- **Testing**: Verify that your application functions as expected.
- **Monitoring**: Set up monitoring to track performance and errors.
- **Scaling**: Plan for scaling based on user demand.

By following this guide, you can deploy your CrewAI project using the method that best fits your requirements. 