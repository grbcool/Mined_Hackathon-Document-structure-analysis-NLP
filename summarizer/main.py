import uvicorn
from fastapi import FastAPI
import dill as pickle
import text_summ
from summ_bm import summ_bm
import json

app = FastAPI()
pickle_in = open("summarizer.pickle","rb")
summarizer=pickle.load(pickle_in)
pickle_in.close()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, post a text to get summary'}

@app.post('/summarizer')
def summarize_text(text: summ_bm):
    text_new=text.dict()
    text_req=text_new['text']
    text_req=text_req.split()
    return {summarizer(text_req)[0]}

if __name__ == '__main__':
    
    uvicorn.run(app, host='127.0.0.1', port=8000)
