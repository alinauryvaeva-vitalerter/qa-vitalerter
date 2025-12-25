pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Oleina/qa-ui-vitalerter.git'
            }
        }

        stage('Install dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                bat 'pytest -v'
            }
        }
    }
}
