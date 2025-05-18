import requests
from bs4 import BeautifulSoup

def get_text(text: str, token: str):
    token = f'Bearer {token}'
    headers = {'Authorization': token}
    
    response = requests.get(
        'https://api.genius.com/search',
        params={'q': text},
        headers=headers
    )
    
    data = response.json()
    url = data['response']['hits'][0]['result']['url']
    
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    
    lyrics_blocks = soup.find_all('div', attrs={'data-lyrics-container': True})
    
    full_text = []
    for block in lyrics_blocks:
        for br in block.find_all('br'):
            br.replace_with('\n')
        block_text = block.get_text(separator='\n')
        lines = [line.strip() for line in block_text.split('\n') if line.strip()]
        
        for line in lines:
            if line.startswith('[') and line.endswith(']'):
                full_text.append('')
                full_text.append(line)
            else:
                full_text.append(line)
    
    result = []
    prev_line = None
    for line in full_text:
        if line or (prev_line and prev_line.strip()):
            result.append(line)
        prev_line = line
    
    return '\n'.join(result).strip()
