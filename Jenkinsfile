pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/alinauryvaeva-vitalerter/qa-vitalerter.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'python3 --version || python --version'
                sh 'python3 -m pip install -r requirements.txt || python -m pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'python3 -m pytest -v || python -m pytest -v'
            }
        }
    }
}
