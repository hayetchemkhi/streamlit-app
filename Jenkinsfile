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
                    // Créer l'environnement virtuel s'il n'existe pas et installer les dépendances
                    echo 'Création de l\'environnement virtuel et installation des dépendances'
                    sh '''
                        if [ ! -d "venv" ]; then
                            python3 -m venv venv
                        fi

                        if [ -f "venv/bin/activate" ]; then
                            . venv/bin/activate
                            pip install -r requirements.txt
                        else
                            echo "Erreur : Impossible de créer l'environnement virtuel"
                            exit 1
                        fi
                    '''
                }
            }
        }
    }
}
