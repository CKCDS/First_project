pipeline {
  agent any
  stages {
    stage('Deliver') {
      steps {
        retry(count: 1) {
          sh '''
          whereis python2.7
          whereis pip
     
            
         
          BUILD_ID=DONTKILLME nohup python manage.py runserver 0.0.0.0:8000'''
          
        }

      }
    }
  }
}
