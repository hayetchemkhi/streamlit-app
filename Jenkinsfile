pipeline {
    agent any

    environment {
        // Définir la version de Python
        PYTHON_VERSION = '3.9'
    }

    stages {
        stage('Checkout') {
            steps {
                // Récupérer le code depuis le repository Git
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                script {
                    // Installer Python et pip si nécessaire
                    sh 'sudo apt-get update'
                    sh 'sudo apt-get install -y python${PYTHON_VERSION} python3-pip'
                    sh 'python3 -m pip install --upgrade pip'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Installer les dépendances depuis requirements.txt
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Exécuter les tests unitaires avec pytest
                    sh 'pytest --maxfail=1 --disable-warnings -q'
                }
            }
        }
    }

    post {
        always {
            // Toujours exécuter cette étape, par exemple nettoyage, rapports, etc.
            echo 'Pipeline terminé'
        }

        success {
            echo 'Tests réussis'
        }

        failure {
            echo 'Les tests ont échoué, vérifier les logs.'
        }
    }
}
