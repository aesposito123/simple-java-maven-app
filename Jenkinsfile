pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git "https://github.com/aesposito123/simple-java-maven-app.git"
            }
        }
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def commitAuthor = sh(script: 'git log -1 --pretty=format:%an', returnStdout: true).trim()
                    echo "Git Commit Author: ${commitAuthor}"
                }
                bat "mvn test"
            }
            post {
                // If Maven was able to run the tests, even if some of the test
                // failed, record the test results and archive the jar file.
                success {
                    junit '**/target/surefire-reports/TEST-*.xml'
                    archiveArtifacts 'target/*.jar'
                }
                unsuccessful {
                    emailext body: "Branch: ${GIT_BRANCH} \nCommit: ${GIT_URL}/commit/${GIT_COMMIT}", subject: "${BUILD_TAG} Failed", to: 'aesposito@revenova.com'   
                }
            }
        }
    }
}
