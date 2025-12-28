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
                sh '''
                docker rm -f selenium || true
                docker run -d --name selenium \
                  -p 4444:4444 \
                  --shm-size=2g \
                  selenium/standalone-chrome:latest
                '''
            }
        }

        stage('Run tests in Python container') {
            steps {
                sh '''
                docker run --rm \
                  --network host \
                  -v "$PWD:/tests" \
                  -w /tests \
                  python:3.11 \
                  bash -c "
                    pip install -r requirements.txt &&
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
