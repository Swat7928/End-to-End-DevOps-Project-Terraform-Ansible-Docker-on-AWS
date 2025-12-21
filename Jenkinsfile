stages {

    stage('Checkout Code') {
        steps {
            git branch: 'main',
                url: 'https://github.com/Swat7928/End-to-End-DevOps-Project-Terraform-Ansible-Docker-on-AWS.git'
        }
    }

    stage('Login to Docker Hub') {
        steps {
            withCredentials([usernamePassword(
                credentialsId: 'dockerhub-creds',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_PASS'
            )]) {
                sh '''
                echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                '''
            }
        }
    }

    stage('Build Docker Image') {
        steps {
            sh '''
            docker build -t $IMAGE_NAME:$IMAGE_TAG ansible/app
            '''
        }
    }

    stage('Push Docker Image') {
        steps {
            sh '''
            docker push $IMAGE_NAME:$IMAGE_TAG
            '''
        }
    }
}
