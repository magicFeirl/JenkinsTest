from fastapi import FastAPI


app = FastAPI()

visited_cnt = 0


@app.get('/')
async def root():
    global visited_cnt
    visited_cnt += 1
    
    return f'Welcome to my website. This page has been visited {visited_cnt} times'