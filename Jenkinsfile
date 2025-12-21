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
