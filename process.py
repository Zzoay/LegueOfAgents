
import json


def extract_champion_info(champion_name):
    with open(f"data/zh/champion/{champion_name}.json", 'r', encoding='utf-8') as f:
        champion = json.load(f)

    ret = {}
   
    ret['id'] = champion['id']
    ret['name'] = champion['name']
    ret['title'] = champion['title']
    ret['locale'] = champion['locale']
    ret['champion'] = {
        "race": champion['champion']['races'],
        "roles": champion['champion']['roles'],
        "role": champion['champion']['role'],
        "biography": champion['champion']['biography'],
    }
    ret["related-champions"] = []
    for rel_champ in champion['related-champions']:
        ret["related-champions"].append(
            {
                "name": rel_champ['name'],
                "title": rel_champ['title'],
                "biography": {
                    "short": rel_champ['biography']['short'],
                    "quote": rel_champ['biography']['quote'],
                }
            }
        )

    return ret


def extract_champion_story(champion_name):
    with open(f"data/zh/story/{champion_name}.json", 'r', encoding='utf-8') as f:
        story = json.load(f)
    used_keys = [
        "id",
        "type",
        {"story": ["title", "subtitle", "custom-story-preview", {"story-sections": {"story-sections": "content"}}]}
    ]
    return 

if __name__ == "__main__":
    extract_champion_info("aatrox")