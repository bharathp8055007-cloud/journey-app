pipeline {
    agent any
    environment {
        IMAGE = "bharathp8055/journey-app:${BUILD_NUMBER}"
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE app/'
            }
        }
        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials',
                                                  usernameVariable: 'DH_USER',
                                                  passwordVariable: 'DH_PASS')]) {
                    sh 'echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin'
                    sh 'docker push $IMAGE'
                }
            }
 
          }
          stage('Deploy') {
            steps {
                sh 'kubectl set image deployment/journey-app journey-app=$IMAGE'
                sh 'kubectl rollout status deployment/journey-app --timeout=60s'

                }
            }

      }
}
