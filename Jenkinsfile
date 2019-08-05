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
    sh "/run/media/minwoo/SOFTWARE/sonar-scanner-4.0.0.1744-linux/bin/sonar-scanner"
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
