
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                bat 'docker build -t devops-uat:latest .'
            }
        }

        stage('Run Application') {
            steps {
                bat 'docker run --rm devops-uat:latest'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'python monitoring/evidently_monitor.py'
            }
        }
    }

    post {
        success {
            echo 'UAT pipeline completed successfully!'
        }

        failure {
            echo 'UAT pipeline failed. Check the console output.'
        }
    }
}
