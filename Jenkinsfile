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
                docker run -d --name selenium \
                  -p 4444:4444 \
                  --shm-size=2g \
                  selenium/standalone-chrome:latest
                '''
            }
        }

        stage('Install deps') {
            steps {
                sh '''
                python3 --version
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run login tests') {
            steps {
                sh '''
                pytest tests/test_login_page -v
                '''
            }
        }
    }

    post {
        always {
            sh '''
            docker rm -f selenium || true
            '''
        }
    }
}
