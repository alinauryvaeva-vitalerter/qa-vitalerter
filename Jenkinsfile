pipeline {
    agent {
        docker {
            image 'selenium/standalone-chrome:latest'
        }
    }

    stages {
        stage('Install Python & deps') {
            steps {
                sh '''
                python3 --version || apt update && apt install -y python3 python3-pip
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
