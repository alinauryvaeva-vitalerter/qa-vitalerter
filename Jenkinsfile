pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Start Selenium') {
            steps {
                sh 'docker rm -f selenium || true'
                sh 'docker run -d --name selenium -p 4444:4444 --shm-size=2g selenium/standalone-chrome:latest'
            }
        }

        stage('Run tests in Python container') {
            steps {
                // Используем ${WORKSPACE} для монтирования текущей папки в /app
                sh '''
                docker run --rm --network host \
                -v ${WORKSPACE}:/app \
                -w /app python:3.11 bash -c "
                    pip install -r requirements.txt &&
                    export PYTHONPATH=/app &&
                    pytest tests/test_login_page -v
                "
                '''
            }
        }
    }

    post {
        always {
            sh 'docker rm -f selenium || true'
        }
    }
}