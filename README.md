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


## Adding Update Manifest Job

Head to Jenkins, new item, enter the name of the manifest. In this case, it's the name specified in the trigger stage in the Jenkinsfile. The name should match the build image job for it to be updated. 
In the next page, select this project is parameterized, select add a string parameter and enter the details as shown in the screenshot. Scroll below to the pipeline section and add pipeline from SCM, select Git and enter the github repo containing the deployment manifest file.

![ Adding String Parameter](images/string_parameter.png).


## Building the image

Head to Jenkins dashboard and select the image job, in this case deploy_pyhton_app_2_eks_image and click on build now.
The pipeline will clone the repository, build the image, test the image, push the image to dockerhub and update the manifest file. 
![ Build Image](images/build_image.png).

The console output image tag will change from latest to tag 1 as shown in the screeenshot.
![ Tag 1](images/tag_1.png).

The newly created image can be seen in the dockerhub repo with the tags updated and the time it updated.
![ Tag 1](images/dockerhub_image.png).