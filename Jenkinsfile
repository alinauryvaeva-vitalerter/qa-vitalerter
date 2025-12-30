pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: [
                'All tests',
                'Correct email and password',
                'Incorrect email and password',
                'Login Passwordless',
                'Login with not activated email'
            ],
            description: 'Choose which tests to run'
        )
    }

    environment {
        PYTHONUNBUFFERED = '1'
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
                    "Correct email and password")
                      TEST_PATH="tests/test_login_page/test_correct_email_and_password.py"
                      ;;
                    "Incorrect email and password")
                      TEST_PATH="tests/test_login_page/test_incorrect_email_and_password.py"
                      ;;
                    "Login Passwordless")
                      TEST_PATH="tests/test_login_page/test_login_passwordless.py"
                      ;;
                    "Login with not activated email")
                      TEST_PATH="tests/test_login_page/test_login_with_not_activated_email.py"
                      ;;
                    *)
                      TEST_PATH="tests"
                      ;;
                  esac

                  echo "Running tests from: $TEST_PATH"

                  docker run --rm \
                    --network host \
                    -e BASE_URL=$BASE_URL \
                    -e LOGIN_EMAIL=$LOGIN_EMAIL \
                    -e LOGIN_PASSWORD=$LOGIN_PASSWORD \
                    -v $WORKSPACE:/tests \
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
