from typing import List
import spacy

def extract_entities(text: str, nlp_model) -> tuple:
    """
    Extrae personas, organizaciones sobre text
    """
    doc = nlp_model(text)
    persons = set()
    organizations = set()
    locations = set()

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            persons.add(ent.text)
        elif ent.label_ == "ORG":
            organizations.add(ent.text)
        elif ent.label_ in ["LOC", "GPE"]:
            locations.add(ent.text)

    return list(persons), list(organizations), list(locations)


def extract_entities_batch(news_items: List[dict], nlp_model) -> List[dict]:
    """
    Procesa una lista de documentos con texto limpio y devuelve los resultados con entidades.
    Espera: [{"id": ..., "cleaned_text": ..., "font": ...}]
    Devuelve: [{"id": ..., "persons": [...], "organizations": [...], "locations": [...]}]
    """
    results = []
    for item in news_items:
        persons, orgs, locs = extract_entities(item["cleaned_text"], nlp_model)
        results.append({
            "id": item["id"],
            "persons": persons,
            "organizations": orgs,
            "locations": locs
        })
    return results
