pipeline {
  agent any
  stages {
    stage('Deliver') {
      steps {
        retry(count: 1) {
          sh '''
          if [ ! -d "venv" ]; then
                virtualenv -p /usr/bin/python2.7 venv
                BUILD_ID=DONTKILLME nohup python manage.py runserver 0.0.0.0:8000
                fi

                . venv/bin/activate
                 pip install -i http://pypi.douban.com/simple -r requirements.txt'''
          
        }

      }
    }
  }
}
