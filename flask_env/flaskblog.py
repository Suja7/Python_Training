from flask import Flask, render_template, request
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Emp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    desg = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"{self.name} - {self.desg}"

@app.route("/")
@app.route("/home")
def index():
    return 'Hello'

@app.route("/emps")
def get_emps():
	emps = Emp.query.all()
	output = []

	for emp in emps:
		emp_data = {'name': emp.name, 'Desg':emp.desg}
		output.append(emp_data)
	return {"emps":output}

@app.route('/emps/<id>')
def get_emp(id):
	emp = Emp.query.get_or_404(id)
	return {"name": emp.name, "Desg":emp.desg}

@app.route('/emps', methods=['POST'])
def add_emp():
	emp = Emp(name=request.json["name"], desg=request.json["desg"])
	db.session.add(emp)
	db.session.commit()
	return {'id': emp.id}

@app.route('/emps/<id>', methods=['DELETE'])
def delete_emp(id):
	emp = Emp.query.get_or_404(id)
	if emp is None:
		return {'error':'Not Found'}
	db.session.delete(emp)
	db.session.commit()
	return {'message': 'deleted'}	

if __name__ == '__main__':
	app.run(debug=True)
