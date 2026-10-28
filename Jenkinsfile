
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
        bat 'docker rm -f evidently-report 2>NUL || exit /b 0'
        bat 'docker create --name evidently-report devops-uat:latest python monitoring/evidently_monitor.py'
        bat 'docker start -a evidently-report'
        bat 'docker cp evidently-report:/app/evidently_report.html "%WORKSPACE%\\evidently_report.html"'
        bat 'docker rm evidently-report'
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
}