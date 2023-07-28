# llama-index flask demo

### Notes

This is just a prototype.

### Requires OpenAI API Key.

## install

```
git clone https://github.com/kailashw/llama-index-flask-demo && cd llama-index-flask-demo


pip install -r requirements.txt

```

.................. Getting Ready with DATA .................................

- place your files under data folder in the root.
- each data should have two files. - {name}\_data.json and {name}\_scehma.json

...................................................

## edit the server.py file with your open API key and then run.

```
python3 server.py

```

### Go to browser

http://127.0.0.1:8080/

### example prompt in curl request

```
curl --location 'http://127.0.0.1:8080/search-json' \
--form 'search="list of top 5 deals closed on 2023-09-05"' \
--form 'model="deals"'
```

<b> Note : </b> .vscode file added for debugging support.
