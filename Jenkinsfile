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
                    echo "${BUILD_TAG}"
                    echo "${GIT_COMMITTER_NAME}"
                    emailext body: "Branch: ${GIT_BRANCH} \nCommit: ${GIT_COMMIT} \nLink: ${GIT_URL}/${GIT_COMMIT}", subject: "${BUILD_TAG} Failed", to: 'aesposito@revenova.com'   
                }
            }
        }
    }
}
