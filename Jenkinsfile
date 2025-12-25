pipeline {
    agent {
        docker {
            image 'selenium/standalone-chrome:latest'
        }
    }

    stages {
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
                PYTHONPATH=. pytest tests/test_login_page -v
                '''
            }
        }
    }
}
