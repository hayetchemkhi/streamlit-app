pipeline {
    agent any

    stages {
        // Étape 1 : Cloner le code depuis GitHub
        stage('Cloner le Code') {
            steps {
                git url: 'https://github.com/hayetchemkhi/streamlit-app.git', branch: 'main'

            }
        }
        
        // Étape 2 : Installer les Dépendances (via requirements.txt)
        stage('Installer les Dépendances') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        // Étape 3 : Exécuter les Tests Unitaires avec Pytest
        stage('Exécuter les Tests Unitaires') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }

    post {
        success {
            echo 'Les tests sont réussis !'
        }
        failure {
            echo 'Un ou plusieurs tests ont échoué.'
        }
    }
}

