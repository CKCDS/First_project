pipeline {
  agent any
  stages {
    stage('Deliver') {
      steps {
        retry(count: 1) {
          sh '''
   if [ ! -d "venv" ]; then    virtualenv -p /usr/bin/python2.7 venv
   fi
  . venv/bin/activate
 
     
            
         
          BUILD_ID=DONTKILLME nohup python manage.py runserver 0.0.0.0:8000'''
          
        }

      }
    }
  }
}
