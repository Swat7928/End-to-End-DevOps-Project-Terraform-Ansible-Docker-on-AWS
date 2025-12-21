pipeline {
    agent any

    environment {
        IMAGE_NAME = "swat7928/learning-app"
        IMAGE_TAG  = "latest"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME:$IMAGE_TAG ansible/app
                '''
            }
        }
    }
}
    stage('Push Docker Image') {
        steps {
            withCredentials([usernamePassword(
                credentialsId: 'dockerhub-creds',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_PASS'
            )]) {
                sh '''
                echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                docker push $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
    }
