pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "nandhu1332/casestudy"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Nandhu1332/casestudy.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh 'docker login -u kadarinandhini -p admin@123'
                sh 'docker push $DOCKER_IMAGE:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
