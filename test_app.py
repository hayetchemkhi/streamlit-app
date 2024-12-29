import pytest
import pandas as pd
from votre_fichier import authenticate, hash_password, load_users, save_user

# Préparer un utilisateur fictif pour les tests
@pytest.fixture
def setup_users():
    # Supprimer le fichier users.csv si présent pour recréer un environnement propre
    try:
        users = pd.read_csv("users.csv")
        users = users[users["username"] != "testuser"]
        users.to_csv("users.csv", index=False)
    except FileNotFoundError:
        pass

    # Créer un nouvel utilisateur pour les tests
    save_user("testuser", "password123")
    
    yield
    # Nettoyage après les tests
    users = pd.read_csv("users.csv")
    users = users[users["username"] != "testuser"]
    users.to_csv("users.csv", index=False)


def test_authenticate_valid(setup_users):
    """Test de la fonction authenticate avec des identifiants valides"""
    assert authenticate("testuser", "password123") == True


def test_authenticate_invalid_password(setup_users):
    """Test de la fonction authenticate avec un mot de passe incorrect"""
    assert authenticate("testuser", "wrongpassword") == False


def test_authenticate_invalid_user(setup_users):
    """Test de la fonction authenticate avec un nom d'utilisateur incorrect"""
    assert authenticate("nonexistentuser", "password123") == False
def test_save_user_new_user():
    """Test de la fonction save_user pour un nouvel utilisateur"""
    # Enlever les utilisateurs existants dans le fichier avant le test
    users = pd.read_csv("users.csv") if "users.csv" in locals() else pd.DataFrame(columns=["username", "password"])
    users = users[users["username"] != "newuser"]
    users.to_csv("users.csv", index=False)

    # Enregistrer un nouvel utilisateur
    result = save_user("newuser", "password123")
    assert result == True
    # Vérifier que l'utilisateur est bien ajouté
    users = pd.read_csv("users.csv")
    assert "newuser" in users["username"].values


def test_save_user_existing_user():
    """Test de la fonction save_user pour un utilisateur existant"""
    # Ajouter un utilisateur existant pour tester la condition de duplicata
    save_user("existinguser", "password123")
    
    # Tenter d'enregistrer le même utilisateur
    result = save_user("existinguser", "newpassword")
    assert result == False
    # Vérifier que le mot de passe n'a pas changé
    users = pd.read_csv("users.csv")
    assert users[users["username"] == "existinguser"]["password"].values[0] != "newpassword"
