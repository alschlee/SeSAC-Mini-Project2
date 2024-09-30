from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "루트 경로 접근 성공"}

@app.get("/data")
async def read_data():
    return {"message": "안녕하세요! 저는 2002년 7월 13일에 태어났고, 음악 듣는 것을 좋아해요."}
