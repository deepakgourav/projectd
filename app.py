from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_salary():
    total_salary_before_tax = None
    tax_deduction = None
    net_salary = None

    if request.method == 'POST':
        # Get user inputs
        hours_per_day = float(request.form['hours_per_day'])
        days_in_month = int(request.form['days_in_month'])
        overtime_hours = float(request.form['overtime_hours'])
        regular_rate = float(request.form['regular_rate'])
        overtime_rate = float(request.form['overtime_rate'])
        monthly_bonus = float(request.form['monthly_bonus'])
        annual_bonus = float(request.form['annual_bonus'])
        working_days_in_year = int(request.form['working_days_in_year'])
        tax_rate = float(request.form['tax_rate'])

        # Calculate regular salary
        regular_hours = hours_per_day * days_in_month
        regular_salary = regular_hours * regular_rate

        # Calculate overtime salary
        overtime_salary = overtime_hours * (overtime_rate * regular_rate)

        # Total salary before tax
        total_salary_before_tax = regular_salary + overtime_salary + monthly_bonus + (annual_bonus / 12)

        # Calculate tax deductions
        tax_deduction = total_salary_before_tax * (tax_rate / 100)

        # Calculate net salary after tax
        net_salary = total_salary_before_tax - tax_deduction

    return render_template('index.html', total_salary_before_tax=total_salary_before_tax, 
                           tax_deduction=tax_deduction, net_salary=net_salary)

if __name__ == '__main__':
    app.run(debug=True)
