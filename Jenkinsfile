pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    stages {

        stage('Start Selenium') {
            steps {
                sh '''
                docker run -d \
                  -p 4444:4444 \
                  --shm-size=2g \
                  selenium/standalone-chrome:latest
                '''
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                python --version
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run login tests') {
            steps {
                sh '''
                PYTHONPATH=. pytest tests/test_login_page -v
                '''
            }
        }
    }

    post {
        always {
            sh 'docker rm -f $(docker ps -aq --filter ancestor=selenium/standalone-chrome) || true'
        }
    }
}
