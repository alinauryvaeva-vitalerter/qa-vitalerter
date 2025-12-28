pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = "1"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
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
                  -e BASE_URL \
                  -e LOGIN_EMAIL \
                  -e LOGIN_PASSWORD \
                  -v "$PWD:/tests" \
                  -w /tests \
                  python:3.11-bullseye bash -c "
                    apt-get update &&
                    apt-get install -y chromium chromium-driver &&
                    pip install -r requirements.txt &&
                    pytest -v
                  "
                '''
            }
        }
    }
}
