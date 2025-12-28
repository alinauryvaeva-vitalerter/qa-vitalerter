pipeline {
    agent any

    environment {
        SELENIUM_IMAGE = "selenium/standalone-chrome:latest"
        PYTHON_IMAGE   = "python:3.11"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Start Selenium') {
            steps {
                sh '''
                docker rm -f selenium || true
                docker run -d \
                  --name selenium \
                  -p 4444:4444 \
                  --shm-size=2g \
                  selenium/standalone-chrome:latest
                '''
            }
        }

        stage('Run tests') {
            environment {
                BASE_URL = credentials('BASE_URL')
                LOGIN_EMAIL = credentials('LOGIN_EMAIL')
                LOGIN_PASSWORD = credentials('LOGIN_PASSWORD')
            }

            steps {
                sh '''
                docker run --rm \
                  --network host \
                  -v "$WORKSPACE:/tests" \
                  -w /tests \
                  -e BASE_URL \
                  -e LOGIN_EMAIL \
                  -e LOGIN_PASSWORD \
                  python:3.11 bash -c "
                    pip install -r requirements.txt &&
                    pytest -v
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
