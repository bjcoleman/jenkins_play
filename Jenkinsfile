pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
                sh 'pytest'
            }
        }
    }
  post
  {
   always
   {
      sh 'echo "\n\n\n\nbye\n\n\n\n"'
   }
 }
}
