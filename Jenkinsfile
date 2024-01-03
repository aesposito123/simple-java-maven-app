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
                    script {
                        commitAuthor = powershell 'git --no-pager show -s --format=\\\'%an\\\' $GIT_COMMIT'
                        echo "${commitAuthor}"
                        emailext body: "Branch: ${commitAuthor} \nCommit: ${GIT_URL}/commit/${GIT_COMMIT}", subject: "${BUILD_TAG} Failed", to: 'aesposito@revenova.com'
                    }
                }
            }
        }
    }
}
