  
node {
    def app

    stage('Access AWS EC2 instance') {
        echo "Start accessing AWS EC2"
        sh "ssh -i /Desktop/test/key1.pem ubuntu@ec2-3-0-61-6.ap-southeast-1.compute.amazonaws.com"
        // sshPublisher(publishers: [sshPublisherDesc(configName: 'ec2', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'apt-get update', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '*. war')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
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

    stage('Deploy image') {
        
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