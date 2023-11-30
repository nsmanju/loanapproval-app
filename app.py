from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_loan_approval_risk(credit_score, income, loan_amount, loan_term, age):
    # ... (same implementation of the loan approval function)

    @app.route('/')
    def index():
        return render_template('index.html')

@app.route('/loan_approval', methods=['POST'])
def loan_approval():
    credit_score = int(request.form['credit_score'])
    income = int(request.form['income'])
    loan_amount = int(request.form['loan_amount'])
    loan_term = int(request.form['loan_term'])
    age = int(request.form['age'])

    decision, overall_score = calculate_loan_approval_risk(credit_score, income, loan_amount, loan_term, age)
    return render_template('result.html', decision=decision, overall_score=overall_score)

if __name__ == '__main__':
    app.run(debug=True)
