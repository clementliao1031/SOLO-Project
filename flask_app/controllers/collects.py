from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.collect import Collect
from flask_app.models.user import User

@app.route('/new/collect')
def new_collect():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_collect.html',user=User.get_by_id(data))


@app.route('/create/collect',methods=['POST'])
def create_collect():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Collect.validate_collect(request.form):
        return redirect('/new/collect')
    data = {
        "name": request.form["name"],
        "review": request.form["review"],
        "pro_con": request.form["pro_con"],
        "pass_buy": int(request.form["pass_buy"]),
        "date_purchase": request.form["date_purchase"],
        "user_id": session["user_id"]
    }
    Collect.save(data)
    return redirect('/dashboard')

@app.route('/edit/collect/<int:id>')
def edit_collect(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_collect.html",edit=Collect.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/collect',methods=['POST'])
def update_collect():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Collect.validate_collect(request.form):
        return redirect('/new/collect')
    data = {
        "name": request.form["name"],
        "review": request.form["review"],
        "pro_con": request.form["pro_con"],
        "pass_buy": int(request.form["pass_buy"]),
        "date_purchase": request.form["date_purchase"],
        "user_id": session["user_id"]
    }
    Collect.update(data)
    return redirect('/dashboard')

@app.route('/collect/<int:id>')
def show_collect(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_collect.html",collect=Collect.get_one(data),user=User.get_by_id(user_data))

@app.route('/destroy/collect/<int:id>')
def destroy_collect(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Collect.destroy(data)
    return redirect('/dashboard')