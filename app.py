from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_loan_approval_risk(credit_score, income, loan_amount, loan_term, age):
    # Define parameters and weights for loan approval decision
    credit_score_weight = 0.4
    income_weight = 0.3
    loan_amount_weight = 0.2
    loan_term_weight = 0.1

    # Calculate the overall score based on the given weights and factors
    calculated_overall_score = (
        credit_score_weight * credit_score +
        income_weight * income +
        loan_amount_weight * loan_amount +
        loan_term_weight * loan_term
    )

    # Define the minimum values needed for loan approval
    min_credit_score = 600
    min_income = 250000
    min_loan_amount = 10000
    min_loan_term = 12
    min_age = 18

    # Rules for loan approval
    if (
        credit_score >= min_credit_score and
        income >= min_income and
        loan_amount >= min_loan_amount and
        loan_term >= min_loan_term and
        age >= min_age
    ):
        if calculated_overall_score >= 0.7:  # You can adjust the threshold according to bank policy
            decision = "Approved"
        else:
            decision = "Conditional Approval"
    else:
        decision = "Rejected"

    return decision, calculated_overall_score

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
