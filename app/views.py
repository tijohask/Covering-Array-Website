# views.py

from flask import render_template
from flask import request

from app import app

from .MasterFile import switch

@app.route('/')
def index():
  return render_template("front_end.html")
    
@app.route('/calc', methods = ['POST'])
def calc():
  data = request.get_json()
  print(request.data)
  give = switch(data["k_level"], data["num_inter"], 4) 
  print(give)
  return give
#request.data
#switch(request.data["k_level"], request.data["num_inter"], 4)
