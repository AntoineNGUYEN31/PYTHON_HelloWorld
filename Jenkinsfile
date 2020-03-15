properties([
    buildDiscarder(logRotator(daysToKeepStr: '3', numToKeepStr: '3')),
])

node('slave-local'){
  stage('Checkout'){
    echo env.BRANCH_NAME
    if (env.BRANCH_NAME == 'develop') {
      checkout scm
    }
    if (env.BRANCH_NAME == 'master') {
      checkout scm
    }
  }
  stage('Compile'){
    sh "docker build -t 192.168.1.55:8082/devops-docker-image/my-dash-app:latest ."
  }
  stage('Test'){
    echo "done"
  }
  stage('Sonarqube'){
    //sh "/run/media/minwoo/SOFTWARE/sonar-scanner-4.0.0.1744-linux/bin/sonar-scanner -X"
    //input 'wait'
    echo "Done"
  }
  stage('Deploy Artifactory JCR'){
    sh "docker push 192.168.1.55:8082/devops-docker-image/my-dash-app:latest"
  }
  stage('Deploy to Prod'){
    sh "docker stop my-dash-app"
    sh "yes|docker container prune"
    sh "docker run --name my-dash-app -p 80:8050 -d 192.168.1.55:8082/devops-docker-image/my-dash-app:latest"
  }
}
