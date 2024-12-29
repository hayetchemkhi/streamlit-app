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
                    sh 'sudo apt-get install -y python3.9 python3-pip python3.9-distutils'

                    // Vérifier l'installation de Python et pip
                    sh 'python3.9 --version'
                    sh 'python3.9 -m pip --version'
                }
            }
        }

        stage('Create Virtual Environment') {
            steps {
                script {
                    // Créer un environnement virtuel
                    sh 'python3.9 -m venv venv'

                    // Activer l'environnement virtuel
                    sh '. venv/bin/activate'
                }
            }
        }
         stage('Install/Update Dependencies') {
    steps {
        sh 'pip install numpy==1.23.0 pandas==1.5.3'
    }
}

        stage('Install Dependencies') {
            steps {
                script {
                    // Installer les dépendances depuis requirements.txt dans l'environnement virtuel
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Exécuter les tests unitaires avec pytest dans l'environnement virtuel
                    sh '. venv/bin/activate && pytest --maxfail=1 --disable-warnings -q'
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
