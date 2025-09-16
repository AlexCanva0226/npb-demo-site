from fastapi import FastAPI
import pandas as pd
import joblib
import os

app = FastAPI(title="NPB Demo Predictor")

MODEL_PATH = "models/model.txt"
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None

@app.get("/predict")
def predict(home_team: str, away_team: str):
    df = pd.read_csv("data/sample_games.csv")
    # 特徴量はサンプルCSVに合わせる
    X = df[['home_start_era','away_start_era','home_recent_winrate','away_recent_winrate','home_field_factor']]
    if model is None:
        return {"error":"モデルがありません。models/model.txt を作成してください"}
    prob = model.predict(X)[0]
    return {"home_team": home_team, "away_team": away_team, "home_win_prob": float(prob)}
