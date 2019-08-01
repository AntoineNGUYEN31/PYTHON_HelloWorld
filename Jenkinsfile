node('slave-local'){
  stage('build'){
    checkout scm
  }
  stage('sonar'){
    sh "sonar-scanner"
    input 'wait'
  }
}
