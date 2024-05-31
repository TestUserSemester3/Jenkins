pipeline {
    agent any

    stages {
        stage('Run tests') {
            steps {
                script {
                    // Run the unit tests
                    sh 'python3 -m unittest test_add.py >> /home/infrastuct/result.txt'
                }
            }
        }
    }
}
