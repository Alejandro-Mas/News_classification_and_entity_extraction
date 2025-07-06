import spacy
import logging
from typing import List

def extract_entities(text: str, ner_model) -> tuple:
    """
    Extrae personas, organizaciones sobre text
    """
    ner = ner_model(text)
    persons = set()
    organizations = set()
    locations = set()

    for ent in ner.ents:
        if ent.label_ == "PERSON":
            persons.add(ent.text)
        elif ent.label_ == "ORG":
            organizations.add(ent.text)
        elif ent.label_ in ["LOC", "GPE"]:
            locations.add(ent.text)

    return list(persons), list(organizations), list(locations)


def extract_entities_batch(news_items: List[dict]) -> List[dict]:
    ner_model = spacy.load("en_core_web_sm")
    """
    Procesa una lista de documentos con texto limpio y devuelve los resultados con entidades.
    Espera: [{"id": ..., "cleaned_text": ...]
    Devuelve: [{"id": ..., "persons": [...], "organizations": [...], "locations": [...]}]
    """
    results = []
    for item in news_items:
        persons, orgs, locs = extract_entities(item["cleaned_text"], ner_model)
        results.append({
            "id": item["id"],
            "persons": persons,
            "organizations": orgs,
            "locations": locs
        })
    return results
