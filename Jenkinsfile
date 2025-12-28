pipeline {
    agent any
    environment {
        // Если переменные не в Credentials, можно задать их тут для теста:
        EMAIL = 'your_real_email@test.com'
        PASSWORD = 'your_real_password'
    }
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
                sh 'sleep 5' // Даем Selenium время запуститься
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