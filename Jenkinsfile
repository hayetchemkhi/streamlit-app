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
                    // Vérifier si le répertoire venv existe, sinon le créer
                    if (!fileExists('venv')) {
                        echo 'Création de l\'environnement virtuel venv'
                        sh 'python3 -m venv venv'  // Créer l'environnement virtuel
                    }
                    // Installer les dépendances
                    echo 'Activation de l\'environnement virtuel et installation des dépendances'
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }
    }
}
