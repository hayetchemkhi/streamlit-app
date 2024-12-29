pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Installer les Dépendances') {
            steps {
                script {
                    // Créer l'environnement virtuel si nécessaire
                    if (!fileExists('venv')) {
                        sh 'python3 -m venv venv'
                    }
                    // Activer l'environnement virtuel et installer les dépendances
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }
    }
}
