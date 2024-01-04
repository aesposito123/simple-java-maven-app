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
                powershell "mvn test -Punit"
            }
            post {
                success {
                    cleanWs cleanWhenAborted: false, cleanWhenFailure: false, cleanWhenNotBuilt: false, cleanWhenUnstable: false                
                }
                unsuccessful {
                    script {
                        def commitAuthor = powershell(script: 'git log -1 --pretty=format:%an', returnStdout: true).trim()
                        emailext body: "Author: ${commitAuthor} \nProject Revenova/tmsMain \nBranch: ${GIT_BRANCH} \nCommit: ${GIT_URL}/commit/${GIT_COMMIT} \nBuild: ${BUILD_URL}", subject: "Jenkins ${JOB_BASE_NAME} ${BUILD_DISPLAY_NAME} Failed", to: 'aesposito@revenova.com'
                        // TODO extract test results if needed
                    }
                }
            }
        }
    }
}
