pipeline {
    agent any
    environment {
        // Укажи здесь реальные данные, если не используешь Jenkins Credentials
        EMAIL = 'your_real_email@example.com'
        PASSWORD = 'your_real_password'
    }
    stages {
        stage('Start Selenium') {
            steps {
                sh 'docker rm -f selenium || true'
                sh 'docker run -d --name selenium -p 4444:4444 --shm-size=2g selenium/standalone-chrome:latest'
                sh 'sleep 10' // Ждем полной готовности Chrome
            }
        }
        stage('Run tests') {
            steps {
                sh '''
                docker run --rm --network host \
                -e EMAIL=${EMAIL} \
                -e PASSWORD=${PASSWORD} \
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