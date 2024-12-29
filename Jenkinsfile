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
                    echo 'Création de l\'environnement virtuel et installation des dépendances'
                    sh '''
                        # Vérification de Python3
                        if ! command -v python3 &> /dev/null; then
                            echo "Python3 non trouvé. Installation..."
                            sudo apt update
                            sudo apt install python3 python3-venv -y
                        fi

                        # Création du venv
                        if [ ! -d "venv" ]; then
                            python3 -m venv venv
                        fi

                        # Activation du venv
                        if [ -f "venv/bin/activate" ]; then
                            . venv/bin/activate
                            pip install -r requirements.txt
                        else
                            echo "Erreur : Échec de la création de venv"
                            exit 1
                        fi
                    '''
                }
            }
        }
    }
}
