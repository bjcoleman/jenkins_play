pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
				sh 'echo "\n\n\n\nhello\n\n\n\n"'
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