
from prompts import PROMPT_FOR_CHAR_CHAT_ZH
from process import extract_champion_info
from utils import get_response


def character_chat(champion_name, turns):
    messages = [
        {"role": "system", "content": PROMPT_FOR_CHAR_CHAT_ZH.format(info=str(extract_champion_info(champion_name)))},
        {"role": "user", "content": input('user: ')},
    ]
    for i in range(turns):
        reponse, total_tokens = get_response(messages)
        print(f"{champion_name}: " + reponse)
        messages.append({"role": "assistant", "content": reponse})
        if total_tokens > 3700:
            messages.pop(1); messages.pop(1)  # pop the first two messages
        user_input = input("\nuser: ")
        messages.append({"role": "user", "content": user_input})
    reponse, total_tokens = get_response(messages)
    print(f"{champion_name}: "  + reponse)

def story_gen():
    prompt = """
    """

    return


if __name__ == "__main__":
    character_chat("aatrox", turns=3)  # 3 in default