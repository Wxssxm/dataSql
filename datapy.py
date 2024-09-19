import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",      # Adresse du serveur
    user="root",           # Nom d'utilisateur
    password="",           # Mot de passe
    database="ecole"       # Base de données
)

cursor = conn.cursor()

# Exemple d'exécution d'une requête SQL
# cursor.execute("""
#     SELECT 
#         e.prenom AS prenom_etudiant, 
#         e.nom AS nom_etudiant, 
#         ens.prenom AS prenom_enseignant, 
#         ens.nom AS nom_enseignant, 
#         e.numero_classe 
#     FROM etudiants e
#     JOIN enseignants ens 
#     ON e.numero_classe = ens.numero_classe
#     """)
# data = cursor.fetchall()
# for row in data:
#     print(row)


def jointure():
    cursor.execute("""
        SELECT e.prenom, e.nom, ens.prenom, ens.nom, e.numero_classe
        FROM etudiants e
        JOIN enseignants ens 
        ON e.numero_classe = ens.numero_classe
    """)
    data = cursor.fetchall()
    for row in data:
        print(row)


def select_eleve():
    cursor.execute("SELECT * FROM etudiants")
    data = cursor.fetchall()
    for row in data:
        print(row)


def compteeleve():
    cursor.execute("""
        SELECT ens.nom, COUNT(*) 
        FROM etudiants e
        JOIN enseignants ens 
        ON e.numero_classe = ens.numero_classe 
        GROUP BY ens.nom
    """)
    data = cursor.fetchall()
    eclass = []
    for row in data:
        eclass.append(  {
             "name": row[0],
            "nbEleve" : row[1]
                })
           
        
    print(eclass)


print("\nNombre d'élèves par enseignant:")
compteeleve()

# Fermer le curseur et la connexion
cursor.close()
conn.close()
