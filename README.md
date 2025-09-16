NPB Demo Site
=============
デモ用の日本プロ野球勝率予測サイトです。
- データはサンプルCSVを使用
- FastAPIでAPI提供
- Reactフロントで勝率表示
- Dockerでまとめて動作可能

手順:
1. Dockerがある場合: `docker-compose up --build`
2. APIアクセス: http://localhost:8000/predict?home_team=Hanshin&away_team=Yomiuri
3. フロントアクセス: http://localhost:3000
