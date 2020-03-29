  
node {
    def app

    stage('Clone repository') {
        /* Cloning the Repository to our Workspace */
        echo "Clone from github"
        checkout scm
    }    

    stage('Build image') {
        /* This builds the actual image */
        echo "Build docker images"
        app = docker.build("kennykwekjy/jenkins")
    }
    
    stage('Test image') {
        
        app.inside {
            sh 'python test.py'
        }
    }

    stage('Push image') {    
        /*      
			You would need to first register with DockerHub before you can push images to your account.
		*/
        docker.withRegistry('https://registry.hub.docker.com/', 'docker-hub') {
            app.push("${env.BUILD_NUMBER}")
            // app.push("latest")
            } 
        echo "Trying to Push Docker Build to DockerHub"
    }

}