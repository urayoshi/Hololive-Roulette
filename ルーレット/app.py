from flask import Flask, render_template, request, jsonify
import csv, random

app = Flask(__name__)

# TSVファイルを読み込む関数
def load_talent_data():
    talents = []
    with open("holomen-list.tsv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            talents.append({
                "name": row["name"].strip(),
                "color": row["color"].strip()
            })
    return talents


@app.route("/")
def index():
    talents = load_talent_data()
    return render_template("roulette.html", talents=talents)


# 抽選処理API
@app.route("/spin", methods=["POST"])
def spin():
    data = request.get_json()
    count = int(data["count"])
    allow_dup = data["allowDup"]

    talents = load_talent_data()
    results = []
    pool = talents.copy()

    for _ in range(count):
        if not pool:
            break
        choice = random.choice(pool)
        results.append(choice)
        if not allow_dup:
            pool.remove(choice)

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

