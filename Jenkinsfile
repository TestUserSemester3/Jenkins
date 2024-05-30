pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                script {
                    // Install the required dependencies
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    // Run the unit tests
                    sh 'python -m unittest discover -s tests'
                }
            }
        }
    }

    post {
        always {
            junit 'tests/test-results.xml'
        }
    }
}
