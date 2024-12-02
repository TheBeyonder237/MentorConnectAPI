from fastapi import APIRouter, HTTPException
from models import ParrainageRequest
from data import data
import random

router = APIRouter()

# Initialiser les structures de parrainage
parrainage = {
    "B2": {},  
    "B3": {},   
    "M1": {},
    "M2": {}
}

def distribuer_parrainage_b1_b2():
    b1_list = data["B1A"] + data["B1B"] + data["B1C"]
    b2_list = data["B2A"] + data["B2B"]

    limite_b2 = -(-len(b1_list) // len(b2_list)) if b2_list else 0  # B1 → B2

    b2_index = 0
    for filleul in b1_list:
        while len(parrainage["B2"].get(b2_list[b2_index], [])) >= limite_b2:
            b2_index = (b2_index + 1) % len(b2_list)
        parrain = b2_list[b2_index]
        parrainage["B2"].setdefault(parrain, []).append(filleul)
        

def distribuer_parrainage_b2_b3():
    b2_list = data["B2A"] + data["B2B"]
    b3_list = data["B3"]

    limite_b3 = -(-len(b2_list) // len(b3_list)) if b3_list else 0  # B2 → B3

    b3_index = 0
    for filleul in b2_list:
        while len(parrainage["B3"].get(b3_list[b3_index], [])) >= limite_b3:
            b3_index = (b3_index + 1) % len(b3_list)
        parrain = b3_list[b3_index]
        parrainage["B3"].setdefault(parrain, []).append(filleul)


def distribuer_parrainage_b3_m1():
    b3_list = data["B3"]
    m1_list = data["M1"]

    limite_m1 = -(-len(b3_list) // len(m1_list)) if m1_list else 0  # B3 → M1

    m1_index = 0
    for filleul in b3_list:
        while len(parrainage["M1"].get(m1_list[m1_index], [])) >= limite_m1:
            m1_index = (m1_index + 1) % len(m1_list)
        parrain = m1_list[m1_index]
        parrainage["M1"].setdefault(parrain, []).append(filleul)


def distribuer_parrainage_m1_m2():
    m1_list = data["M1"]
    m2_list = data["M2"]

    limite_m2 = -(-len(m1_list) // len(m2_list)) if m2_list else 0  # M1 → M2

    m2_index = 0
    for filleul in m1_list:
        while len(parrainage["M2"].get(m2_list[m2_index], [])) >= limite_m2:
            m2_index = (m2_index + 1) % len(m2_list)
        parrain = m2_list[m2_index]
        parrainage["M2"].setdefault(parrain, []).append(filleul)


# Route pour B1 → B2
@router.post("/parrainage/b1-b2/auto/random/")
def parrainage_b1_b2_random():
    # Liste des B1 et B2
    b1_list = data["B1A"] + data["B1B"] + data["B1C"]
    b2_list = data["B2A"] + data["B2B"]

    # Limite des parrainages par parrain
    limite_b2 = -(-len(b1_list) // len(b2_list)) if b2_list else 0  # B1 → B2

    random.shuffle(b1_list)  # Mélanger les B1 de manière aléatoire
    b2_index = 0  # Indice du parrain B2

    for filleul in b1_list:
        # Trouver un parrain qui n'a pas atteint la limite
        while len(parrainage["B2"].get(b2_list[b2_index], [])) >= limite_b2:
            b2_index = (b2_index + 1) % len(b2_list)
        parrain = b2_list[b2_index]
        parrainage["B2"].setdefault(parrain, []).append(filleul)

    return {"message": "Le parrainage aléatoire de B1 vers B2 a été effectué avec succès !", "parrainage": parrainage["B2"]}


# Route pour B2 → B3
@router.post("/parrainage/b2-b3/auto/random/")
def parrainage_b2_b3_random():
    # Liste des B2 et B3
    b2_list = data["B2A"] + data["B2B"]
    b3_list = data["B3"]

    # Limite des parrainages par parrain
    limite_b3 = -(-len(b2_list) // len(b3_list)) if b3_list else 0  # B2 → B3

    random.shuffle(b2_list)  # Mélanger les B2 de manière aléatoire
    b3_index = 0  # Indice du parrain B3

    for filleul in b2_list:
        # Trouver un parrain qui n'a pas atteint la limite
        while len(parrainage["B3"].get(b3_list[b3_index], [])) >= limite_b3:
            b3_index = (b3_index + 1) % len(b3_list)
        parrain = b3_list[b3_index]
        parrainage["B3"].setdefault(parrain, []).append(filleul)

    return {"message": "Le parrainage aléatoire de B2 vers B3 a été effectué avec succès !", "parrainage": parrainage["B3"]}


@router.post("/parrainage/b3-m1/auto/random/")
def parrainage_b3_m1_random():
    # Liste des B3 et M1
    b3_list = data["B3"]
    m1_list = data["M1"]

    # Limite des parrainages par parrain
    limite_m1 = -(-len(b3_list) // len(m1_list)) if m1_list else 0  # B3 → M1

    random.shuffle(b3_list)  # Mélanger les B3 de manière aléatoire
    m1_index = 0  # Indice du parrain M1

    for filleul in b3_list:
        # Trouver un parrain qui n'a pas atteint la limite
        while len(parrainage["M1"].get(m1_list[m1_index], [])) >= limite_m1:
            m1_index = (m1_index + 1) % len(m1_list)
        parrain = m1_list[m1_index]
        parrainage["M1"].setdefault(parrain, []).append(filleul)

    return {"message": "Le parrainage aléatoire de B3 vers M1 a été effectué avec succès !", "parrainage": parrainage["M1"]}



@router.post("/parrainage/m1-m2/auto/random/")
def parrainage_m1_m2_random():
    # Liste des M1 et M2
    m1_list = data["M1"]
    m2_list = data["M2"]

    # Limite des parrainages par parrain
    limite_m2 = -(-len(m1_list) // len(m2_list)) if m2_list else 0  # M1 → M2

    random.shuffle(m1_list)  # Mélanger les M1 de manière aléatoire
    m2_index = 0  # Indice du parrain M2

    for filleul in m1_list:
        # Trouver un parrain qui n'a pas atteint la limite
        while len(parrainage["M2"].get(m2_list[m2_index], [])) >= limite_m2:
            m2_index = (m2_index + 1) % len(m2_list)
        parrain = m2_list[m2_index]
        parrainage["M2"].setdefault(parrain, []).append(filleul)

    return {"message": "Le parrainage aléatoire de M1 vers M2 a été effectué avec succès !", "parrainage": parrainage["M2"]}




# Fonction pour gérer la répartition automatique des filleuls
def distribuer_parrainage_general():
    # Listes des niveaux
    b1_list = data["B1A"] + data["B1B"] + data["B1C"]
    b2_list = data["B2A"] + data["B2B"]
    b3_list = data["B3"]
    m1_list = data["M1"]
    m2_list = data["M2"]

    # Limite des parrainages par parrain
    limite_b2 = -(-len(b1_list) // len(b2_list)) if b2_list else 0  # B1 → B2
    limite_b3 = -(-len(b2_list) // len(b3_list)) if b3_list else 0  # B2 → B3
    limite_m1 = -(-len(b3_list) // len(m1_list)) if m1_list else 0  # B3 → M1
    limite_m2 = -(-len(m1_list) // len(m2_list)) if m2_list else 0  # M1 → M2

    # Mélanger les filles de manière aléatoire pour chaque niveau
    random.shuffle(b1_list)
    random.shuffle(b2_list)
    random.shuffle(b3_list)
    random.shuffle(m1_list)
    random.shuffle(m2_list)

    # Distribution B1 → B2
    b2_index = 0
    for filleul in b1_list:
        while len(parrainage["B2"].get(b2_list[b2_index], [])) >= limite_b2:
            b2_index = (b2_index + 1) % len(b2_list)
        parrain = b2_list[b2_index]
        parrainage["B2"].setdefault(parrain, []).append(filleul)

    # Distribution B2 → B3
    b3_index = 0
    for filleul in b2_list:
        while len(parrainage["B3"].get(b3_list[b3_index], [])) >= limite_b3:
            b3_index = (b3_index + 1) % len(b3_list)
        parrain = b3_list[b3_index]
        parrainage["B3"].setdefault(parrain, []).append(filleul)

    # Distribution B3 → M1
    m1_index = 0
    for filleul in b3_list:
        while len(parrainage["M1"].get(m1_list[m1_index], [])) >= limite_m1:
            m1_index = (m1_index + 1) % len(m1_list)
        parrain = m1_list[m1_index]
        parrainage["M1"].setdefault(parrain, []).append(filleul)

    # Distribution M1 → M2
    m2_index = 0
    for filleul in m1_list:
        while len(parrainage["M2"].get(m2_list[m2_index], [])) >= limite_m2:
            m2_index = (m2_index + 1) % len(m2_list)
        parrain = m2_list[m2_index]
        parrainage["M2"].setdefault(parrain, []).append(filleul)

    return {"message": "Le parrainage général a été effectué avec succès.", "parrainage": parrainage}

@router.post("/parrainage/auto/general/random/")
def parrainage_auto_general_random():
    result = distribuer_parrainage_general()
    return result


@router.get("/parrainage/{niveau}/")
def afficher_parrainage(niveau: str):
    if niveau.upper() in parrainage:
        return {
            "message": f"Voici le parrainage pour le niveau {niveau.upper()}",
            "details": parrainage[niveau.upper()]
        }
    else:
        return {"error": f"Le niveau {niveau} n'existe pas dans le système de parrainage."}