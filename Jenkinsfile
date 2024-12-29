pipeline {
    agent any

    environment {
        // Définir la version de Python que vous voulez utiliser
        PYTHON_VERSION = '3.9'
    }

    stages {
        stage('Checkout') {
            steps {
                // Récupérer le code du repository Git
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                script {
                    // Installer Python et Pip (si ce n'est pas déjà fait)
                    sh 'sudo apt-get update'
                    sh 'sudo apt-get install -y python${PYTHON_VERSION} python3-pip'
                    sh 'python3 -m pip install --upgrade pip'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                // Installer les dépendances à partir du fichier requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Exécuter les tests unitaires avec pytest
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Post Test') {
            steps {
                script {
                    // Vous pouvez ajouter des actions post-test (par exemple, rapports, nettoyage, etc.)
                }
            }
        }
    }

    post {
        always {
            // Toujours exécuter cette étape (par exemple, nettoyage, rapports, etc.)
            echo 'Pipeline terminé'
        }

        success {
            echo 'Tests réussis, déploiement ou autres actions à ajouter ici.'
        }

        failure {
            echo 'Les tests ont échoué, vérifier les logs.'
        }
    }
}
