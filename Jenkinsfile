pipeline {
    agent any

    stages {
        stage('Run tests') {
            steps {
                script {
                    // Run the unit tests
                    sh 'python -m unittest test_add.py'
                }
            }
        }
    }
}
