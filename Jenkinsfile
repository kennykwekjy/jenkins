  
node {
    def app

    stage('Access AWS EC2 instance') {
        echo "Start accessing AWS EC2"
        ssh -i "key1.pem" ubuntu@ec2-3-0-61-6.ap-southeast-1.compute.amazonaws.com
    }

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
            echo "Tests passed"
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