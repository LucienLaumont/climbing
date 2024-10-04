from pydantic import BaseModel
from typing import Optional

# Schéma de base pour les routes (voies d'escalade)
class RouteBase(BaseModel):
    country: str
    crag: str  # Site d'escalade
    sector: str  # Secteur d'escalade
    name: str  # Nom de la voie
    tall_recommend_sum: int = -1  # Recommandation pour les grimpeurs grands, par défaut -1
    grade_mean: float  # Moyenne des notes de difficulté
    cluster: int  # Regroupement ou catégorie de la voie
    rating_tot: float  # Note totale

# Schéma pour la création d'une nouvelle route
class RouteCreate(RouteBase):
    pass

# Schéma pour la réponse avec l'ID de la route
class Route(RouteBase):
    name_id: int  # Identifiant de la voie

    class Config:
        orm_mode = True
