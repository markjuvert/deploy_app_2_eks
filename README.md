# deploy_app_2_eks
Deploying a Python Application to EKS uisng Jenkins and GitOps pipelin


The CICD pipeline starts with creating Jenkins server and installing jenkins. Also install a;; the necessary plugins such as EC2 plugins, github plugins, docker plugins, Parameterized trigger Plugin,  GitHub Integration Plugin and so on.  ![Installing Plugins](images/plugin.png). 

Next, configure EC2 as Jenkins agent. Under manage jenkins, head to manage clouds, configure clouds and fill in all the necessary information.

## Add Credentials
For jenkins to communicate with other services such as github and docker, it needs credentials. Head to manage jenkins, manage credentials, and add the required credentials. ![ Adding Credentials](images/credentials.png).

## Creating the pipeline in Jenkins

In Jenkins, click on new item, enter the name of the pipeline, select pipeline below and click on okay. The next page is the configure page. Scroll down to the pipeline section and select pipeline script from SCM, select Git as the SCM, head to github and copy the repo link and paste it in the repository URL field. IF the repo is a private repo, do add github credentials.
![ Adding Image Pipeline](images/pipeline.png).


## Adding Files to Github Repo
In this step, code and commit all the necessary files to the github repo.![ Adding Files to Github Repo](images/github.png).
