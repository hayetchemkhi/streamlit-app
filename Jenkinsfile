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
                    // Créer l'environnement virtuel et installer les dépendances
                    echo 'Création de l\'environnement virtuel et installation des dépendances'
                    sh '''
                        # Créer l'environnement virtuel s'il n'existe pas
                        if [ ! -d "venv" ]; then
                            python3 -m venv venv
                        fi

                        # Activer l'environnement virtuel et installer les dépendances
                        source venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }
    }
}
