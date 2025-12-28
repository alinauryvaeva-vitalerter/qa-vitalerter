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

    stages {
        stage('Run tests') {
            steps {
                sh """
                if [ "${params.TEST_SUITE}" = "login_positive" ]; then
                    pytest tests/test_login_page/test_correct_email_and_password.py
                elif [ "${params.TEST_SUITE}" = "login_negative" ]; then
                    pytest tests/test_login_page/test_incorrect_email_and_password.py
                else
                    pytest
                fi
                """
            }
        }
    }
}
