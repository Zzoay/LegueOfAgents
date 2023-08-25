
import json

from curl_cffi import requests


def fetch_champions():
    # url = f"{base_url}/zh_CN/champions/"
    url = "https://yz.lol.qq.com/v1/zh_cn/champion-browse/index.json"

    response = requests.get(url, headers=headers, impersonate="chrome110", timeout=500).json()
    print(response["champions"])

    with open("data/zh/champion/champions.json", 'w', encoding='utf-8') as f:
        json.dump(response["champions"], f, ensure_ascii=False, indent=4)
    
    return

def fetch_champion_bios():
    stroy_url = "https://yz.lol.qq.com/zh_CN/story/champion/"
    with open("data/zh/world/champions.json", 'r', encoding='utf-8') as f:
        champions = json.load(f)
    for champion in champions:
        url = f"https://yz.lol.qq.com/v1/zh_cn/champions/{champion['slug']}/index.json"
        response = requests.get(url, headers=headers, impersonate="chrome110", timeout=500).json()
        with open(f"data/zh/champion/{champion['slug']}.json", 'w', encoding='utf-8') as f:
            json.dump(response, f, ensure_ascii=False, indent=4)

    return

def fetch_champion_stories():
    stroy_url = "https://yz.lol.qq.com/zh_CN/story/champion/"
    with open("data/zh/world/champions.json", 'r', encoding='utf-8') as f:
        champions = json.load(f)
    for champion in champions:
        champion = json.load(open(f"data/zh/champion/{champion['slug']}.json", 'r', encoding='utf-8'))
        story_previews = [x for x in champion['modules'] if x['type'] == 'story-preview']
        
        stories = []
        for story_preview in story_previews:
            story_preview.pop('slug')
            story_preview.pop('type')

            url = f"https://yz.lol.qq.com/v1/{story_preview['url']}/index.json"

            response = requests.get(url, headers=headers, impersonate="chrome110", timeout=500)
            if response.status_code == 200:
                content = response.json()
                stories.append(content)
            else:
                print("Url not found: " + url)
                continue
            with open(f"data/zh/story/{champion['id']}.json", 'w', encoding='utf-8') as f:
                json.dump(stories, f, ensure_ascii=False, indent=4)

    return

def fetch_regions():
    # https://yz.lol.qq.com/v1/zh_cn/faction-browse/index.json
    with open("data/zh/world/regions.json", 'r', encoding='utf-8') as f:
        regions = json.load(f)['factions']

    for region in regions:
        url = f"https://yz.lol.qq.com/v1/zh_cn/factions/{region['slug']}/index.json"
        response = requests.get(url, headers=headers, impersonate="chrome110", timeout=500)
        if response.status_code == 200:
            content = response.json()
            with open(f"data/zh/region/{region['slug']}.json", 'w', encoding='utf-8') as f:
                json.dump(content, f, ensure_ascii=False, indent=4)

    return


if __name__ == '__main__':
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    base_url = "https://yz.lol.qq.com"  # ZH_CN
    # fetch_champion_bios()
    fetch_regions()