pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                script {
                    // Mettre à jour la liste des paquets et installer Python 3.9 à partir du PPA deadsnakes
                    sh 'sudo apt-get update'
                    sh 'sudo apt-get install -y software-properties-common'
                    sh 'sudo add-apt-repository ppa:deadsnakes/ppa -y'
                    sh 'sudo apt-get update'
                    sh 'sudo apt-get install -y python3.9 python3-pip'

                    // Installer distutils pour résoudre le problème de module manquant
                    sh 'sudo apt-get install -y python3.9-distutils'

                    // Vérifier l'installation de Python et pip
                    sh 'python3.9 --version'
                    sh 'python3.9 -m pip --version'
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
