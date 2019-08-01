node('slave-local'){
  stage('build'){
    echo env.BRANCH_NAME
    if (env.BRANCH_NAME == 'develop') {
      checkout scm
    }
  }
  stage('sonar'){
    sh "sonar-scanner"
    input 'wait'
  }
}
