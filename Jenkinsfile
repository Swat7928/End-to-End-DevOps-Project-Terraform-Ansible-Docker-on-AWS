pipeline {
    agent any

    environment {
        IMAGE_NAME = "swat7928/learning-app"
        IMAGE_TAG  = "latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/swat7928/End-to-End-DevOps-Project-Terraform-Ansible-Docker-on-AWS.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                docker build -t $IMAGE_NAME:$IMAGE_TAG ansible/app
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
            }
        }
    }
}
