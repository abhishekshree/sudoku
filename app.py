from flask import Flask, render_template, request
# from validity import check_sudoku
from solver import solve

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST', 'GET'])
def get_sudoku():
    sudoku = [[0 for _ in range(9)] for _ in range(9)]
    if request.method == 'POST':
        result = request.form
        for i in range(9):
            for j in range(9):
                val = 9*i+j
                pos = "cell-" + str(val)
                if result[pos] == "":
                    sudoku[i][j] = 0
                else:
                    sudoku[i][j] = int(result[pos])
        # print(sudoku)
        solve(sudoku)
        return render_template("solved.html", sudoku=sudoku)


if __name__ == '__main__':
    app.run()
