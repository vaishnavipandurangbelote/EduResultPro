from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        name = request.form["name"]
        roll = request.form["roll"]

        marks = [
            int(request.form["sub1"]),
            int(request.form["sub2"]),
            int(request.form["sub3"]),
            int(request.form["sub4"]),
            int(request.form["sub5"])
        ]

        total = sum(marks)
        percentage = total / 5

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "F"

        status = "PASS ✅" if percentage >= 40 else "FAIL ❌"

        result = {
            "name": name,
            "roll": roll,
            "total": total,
            "percentage": round(percentage, 2),
            "grade": grade,
            "status": status
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)