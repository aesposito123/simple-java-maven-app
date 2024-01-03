pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git "https://github.com/aesposito123/simple-java-maven-app.git"
            }
        }
        stage('Test') {
            steps {        
                script {
                    GIT_COMMITTER_NAME = $(bat 'git --no-pager show -s --format=\'%an\' $GIT_COMMIT')
                    echo "Git Commit Author: ${GIT_COMMITTER_NAME}"
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
                    emailext body: "Branch: ${GIT_COMMITTER_NAME} \nCommit: ${GIT_URL}/commit/${GIT_COMMIT}", subject: "${BUILD_TAG} Failed", to: 'aesposito@revenova.com'   
                }
            }
        }
    }
}
