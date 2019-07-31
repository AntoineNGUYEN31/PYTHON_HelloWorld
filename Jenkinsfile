node('slave-localhost'){
  stage('build'){
    checkout scm
  }
  stage('sonar'){
    sh "sonar-scanner"
    input 'wait'
  }
}
