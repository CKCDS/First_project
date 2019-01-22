pipeline {
  agent any
  stages {
    stage('Deliver') {
      steps {
        retry(count: 1) {
          sh '''cd First_project
BUILD_ID=DONTKILLME nohup python manage.py runserver 0.0.0.0:8000'''
        }

      }
    }
  }
}