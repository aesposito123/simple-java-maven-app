pipeline {
    // TODO investigate if we need agents
    agent any
    stages {
        stage('Test') {
            steps {        
                powershell "mvn test -Punit"
            }
            post {
                success {
                    steps {
                        echo currentBuild.getPreviousBuild().result
                        script {
                            if('FAILURE' == currentBuild.getPreviousBuild().result) {
                                echo 'last buil failed so send email' 
                            }
                        }
                        echo 'Tests ran successfully'  
                        // TODO anyway to check for a false positive and additonal actions needed in success
                    }
                }
                unsuccessful {
                    script {
                        echo currentBuild.getPreviousBuild().result
                        def commitAuthor = powershell(script: 'git log -1 --pretty=format:%an', returnStdout: true).trim()
                        emailext body: "Author: ${commitAuthor} \nProject Revenova/tmsMain \nBranch: ${GIT_BRANCH} \nCommit: ${GIT_URL}/commit/${GIT_COMMIT} \nBuild: ${BUILD_URL}", 
                                 subject: "Jenkins ${JOB_BASE_NAME} Build ${BUILD_DISPLAY_NAME} Failed",
                                 to: 'aesposito@revenova.com'
                        // TODO extract test results if needed
                        if('FAILURE' == currentBuild.getPreviousBuild().result) {
                            echo 'We fail again' 
                        }
                    }
                }
            }
        }
    }
}
