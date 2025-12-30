pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: [
                'all',
                'login_positive',
                'login_negative'
            ],
            description: 'Which tests to run'
        )
    }

    environment {
        USE_REMOTE_DRIVER = 'true'
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
                BASE_URL       = credentials('BASE_URL')
                LOGIN_EMAIL    = credentials('LOGIN_EMAIL')
                LOGIN_PASSWORD = credentials('LOGIN_PASSWORD')
            }
            steps {
                sh '''
                case "$TEST_SUITE" in
                  all)
                    TEST_PATH="tests"
                    ;;
                  login_positive)
                    TEST_PATH="tests/test_login_page/test_correct_email_and_password.py"
                    ;;
                  login_negative)
                    TEST_PATH="tests/test_login_page/test_login_passwordless.py \
                               tests/test_login_page/test_incorrect_email_and_password.py \
                               tests/test_login_page/test_login_with_not_activated_email.py"
                    ;;
                esac

                docker run --rm \
                  --network host \
                  -e USE_REMOTE_DRIVER=true \
                  -e BASE_URL=$BASE_URL \
                  -e LOGIN_EMAIL=$LOGIN_EMAIL \
                  -e LOGIN_PASSWORD=$LOGIN_PASSWORD \
                  -v $PWD:/tests \
                  -w /tests \
                  python:3.11 bash -c "
                    pip install -r requirements.txt &&
                    pytest -v $TEST_PATH
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
