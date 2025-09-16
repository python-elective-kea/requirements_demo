# Requirements demo
Demo i klassen om requirements, moduler 

## Requirements

```
  pip3 install requests
  pip3 list
  pip3 freeze > requirements.txt
```

## environments variables

Demo api: https://api.github.com/repos/clbokea/osman?

### .env fil
```
API_KEY=123Fhg8JJhuui
```
### script.py
```
  pip install python-dotenv

```
```
  # imports
  from dotenv import load_dotenv
  import os
```
```
  load_dotenv()
  api_key = os.environ.get('API_KEY')
  url = https://api.github.com/repos/clbokea/osman?

  headers = {
        'Authorization': f'token {api_key}'
  }
  response = requests.get(url, headers=headers)
  repo_data = response.json()

```


