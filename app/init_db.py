import json
import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal, BaseSQL, engine
from models import Climber, Route
from schemas import climbers, routes

# Fonction pour initialiser la base de données
def init_db():
    # Créer les tables dans la base de données (si elles n'existent pas déjà)
    BaseSQL.metadata.create_all(bind=engine)

    # Démarrer une session
    db: Session = SessionLocal()

    try:
        # Charger les données des grimpeurs
        climber_data = pd.read_csv('data/climber_df.csv')
        # Charger les données des routes
        route_data = pd.read_csv('data/routes_rated.csv')

        # Ajouter les grimpeurs à la base de données
        for _, row in climber_data.iterrows():
            climber = Climber(
                user_id=row['user_id'],
                country=row['country'],
                sex=row['sex'],
                height=row['height'],
                weight=row['weight'],
                age=row['age'],
                years_cl=row['years_cl'],
                date_first=row['date_first'],
                date_last=row['date_last'],
                grades_count=row['grades_count'],
                grades_first=row['grades_first'],
                grades_last=row['grades_last'],
                grades_max=row['grades_max'],
                grades_mean=row['grades_mean'],
                year_first=row['year_first'],
                year_last=row['year_last']
            )
            db.add(climber)

        # Ajouter les routes à la base de données
        for _, row in route_data.iterrows():
            route = Route(
                name_id=row['name_id'],
                country=row['country'],
                crag=row['crag'],
                sector=row['sector'],
                name=row['name'],
                tall_recommend_sum=row['tall_recommend_sum'],
                grade_mean=row['grade_mean'],
                cluster=row['cluster'],
                rating_tot=row['rating_tot']
            )
            db.add(route)

        # Commit des changements
        db.commit()
    
    except Exception as e:
        db.rollback()
        print(f"Erreur lors de l'initialisation de la base de données : {e}")
    finally:
        db.close()

# Appeler la fonction d'initialisation
if __name__ == "__main__":
    init_db()
