node('slave-local'){
  stage('build'){
    echo env.BRANCH_NAME
    checkout scm
  }
  stage('sonar'){
    sh "sonar-scanner"
    input 'wait'
  }
}
