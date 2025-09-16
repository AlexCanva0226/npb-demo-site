import pandas as pd
import lightgbm as lgb
import joblib
import os

df = pd.read_csv("data/sample_games.csv")
df['home_win'] = (df['home_score'] > df['away_score']).astype(int)
features = ['home_start_era','away_start_era','home_recent_winrate','away_recent_winrate','home_field_factor']
X = df[features]
y = df['home_win']

train_data = lgb.Dataset(X, label=y)
params = {'objective':'binary','metric':'binary_logloss','verbosity':-1}
model = lgb.train(params, train_data, num_boost_round=10)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.txt")
print("モデルを作成しました: models/model.txt")
