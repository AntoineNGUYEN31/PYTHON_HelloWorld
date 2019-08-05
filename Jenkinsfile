node('slave-local'){
  stage('Checkout'){
    echo env.BRANCH_NAME
    if (env.BRANCH_NAME == 'develop') {
      checkout scm
    }
  }
  stage('Compile'){
    echo "done"
  }
  stage('Compile'){
    echo "done"
  }
  stage('sonar'){
    sh "sonar-scanner"
    input 'wait'
  }
  stage('Document'){
    echo "done"
  }
  stage('Deploy'){
    echo "done"
  }
}

//
