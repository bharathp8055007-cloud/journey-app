pipeline{
    agent any
    environment {
         IMAGE = "bharathp8055/journey-app:${BUILD_NUMBER}"
    }
    stages {
        stage('Build')
          steps {
              sh 'docker build -t $IMAGE  app/'
          }
        }
      }
  }
