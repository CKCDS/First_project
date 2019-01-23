pipeline {
  agent any
  stages {
    stage('Deliver') {
      steps {
        retry(count: 1) {
          sh '''
          BUILD_ID=DONTKILLME nohup python manage.py runserver 0.0.0.0:8000'''
          
        }

      }
    }
  }
}
