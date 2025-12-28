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
                pip3 install --user -r requirements.txt
                '''
            }
        }

        stage('Run login tests') {
            steps {
                sh '''
                export PYTHONPATH=$HOME/.local/lib/python3.14/site-packages
                PYTHONPATH=. pytest tests/test_login_page -v
                '''
            }
        }
    }
}
