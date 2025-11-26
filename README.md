🎰 ホロライブルーレット
---
🧪 概要
---
このアプリは、TSVファイルに登録されたホロライブタレント一覧から
ランダムにタレントを抽選できる Flask製のWebアプリ です。

回数指定・重複の許可・タレントカラー表示など、
ガチャやルーレット風の抽選を手軽に楽しめるツールとして作成しました。

🌟 主な機能
---
🔢 抽選回数の指定

1回から最大50回まで、自由に抽選回数を指定できます。

🔄 重複ON / OFF 切り替え

「重複ON」 → 完全ランダムで同じタレントが複数回出現

「重複OFF」 → 同じタレントは1回だけ（ガチャの“単発×n回”のような動作）

🎨 タレントカラー表示
---
TSVに登録された name と color（例 #ffacd3） を読み取り、

抽選結果をタレントカラーのカードとして表示します。

🔗 将来的な拡張：タレントのYouTubeチャンネルへリンク

データに URL 列を追加すれば、カードをクリックして公式チャンネルへジャンプ可能
（コード側に対応済み / 現状は TSV 未登録のためリンクなし）

🧰 使用技術
---
区分	技術
言語	Python
Webフレームワーク	Flask
フロント	HTML / CSS / JavaScript
データ形式	TSV (Tab-Separated Values)
その他	csv モジュール／JSON通信（fetch API）

📁 フォルダ構成
---
<img width="412" height="133" alt="image" src="https://github.com/user-attachments/assets/a7448b79-dbfc-431b-8bd3-41575a4835d5" />

🚀 実行方法
---
1. ライブラリをインストール
pip install flask

2. アプリを起動
python app.py

3. ブラウザでアクセス
http://127.0.0.1:5001

💡 工夫した点
---
1️⃣ TSVデータによる柔軟な管理

タレント名・カラーを Python コードではなく TSV ファイルとして管理することで

新タレント追加

カラー変更

URL追加（拡張）
が即座に行える設計にしています。

2️⃣ fetch API を使用した非同期通信

抽選は /spin に対して JavaScript で POST

結果を JSON で受け取り UI に反映
→ ページリロードなしで動く仕組みを採用

3️⃣ 初学者でも読みやすいコード

ファイル分割（app.py / HTML / TSV）

関数の役割ごとに処理を整理

Jinja2 と JavaScript の混在を避け、見通しをよく設計を意識しました

🖥 画面イメージ
---
<img width="1916" height="910" alt="image" src="https://github.com/user-attachments/assets/7a2e8dbc-2552-455d-81ee-1a946a5be161" />
<img width="1919" height="914" alt="image" src="https://github.com/user-attachments/assets/79338cb8-cd28-4100-9d65-ccacba438c16" />
<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/9a33ce58-3c24-480a-a41e-71e297794482" />



📝 免責事項
--
本アプリは 非公式のファン制作ツール です。
カバー株式会社およびホロライブプロダクションとは一切関係ありません。
