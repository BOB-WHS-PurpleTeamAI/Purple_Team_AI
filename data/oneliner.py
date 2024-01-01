from onelinerizer import onelinerize
import os
path = "C:/Users/catow/OneDrive/바탕 화면/Purple_Team_AI/data"


def onelinecode_generation(code):
    code = code.replace('"', "\\x22")
    if "'" not in code:
        code = f"""{repr(code)}""".replace("!", "\\x21").replace("`", "\\x60").replace("(", "\\x28").replace(")", "\\x29").replace("@", "\\x40")
    return code

file_list = os.listdir(path)
file_list_data = [file for file in file_list if file.endswith('.txt')]
for file in file_list_data:
    f = open(path + "/" + file,'r', encoding='UTF8')
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    f.close()
    f = open(path + "/" +"exploit_code_" + file , 'w', encoding='UTF8')
    for query in lines:
        code = '''def main():
                    url = ""
                    headers = {"Content-Type": "application/json", "Authorization": "Bearer TOKEN"}
                    data = {"query": "'''+query+'''"}
                    try:
                        response = requests.post(url, headers=headers, json=data)
                        response.raise_for_status()
                        print(response.status_code, end="\n")
                        print(response.json())
                    except requests.exceptions.RequestException as e:
                        print(e)'''
        f.writelines(onelinecode_generation(code))
        f.writelines("\n")
    f.close()