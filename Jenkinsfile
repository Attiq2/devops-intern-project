pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',  
                    url:  'https://github.com/Attiq2/devops-intern-project.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t attiq1124/devops-intern-app:v1 -f docker/Dockerfile .'
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-creds', variable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u attiq1124 --password-stdin'
                    sh 'docker push attiq1124/devops-intern-app:v1'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s-manifests/'
            }
        }
    }
}
