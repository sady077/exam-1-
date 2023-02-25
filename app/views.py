from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from sqlalchemy.exc import IntergityError

from . import app, db
from .models import Position, Employee, User
from .forms import PositionForm, EmployeeForm, UserForm

def index():
    employee = Employee.query.all()
    return render_template('index.html', employee=employee)



def position_create():
    position = Position.query.get(id)
    form = PositionForm(obj=position)
    if request.method == 'POST':
        form.populate_obj(position)
        db.session.add(position)
        db.session.commit()

        return redirect(url_for('positions'))
    else:
        print(form.errors)
    return render_template('standart_form.html', form=form)




def employee_create():
    form = EmployeeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            employee = Employee()
            form.populate_obj(employee)
            db.session.add(employee)
            try:
                db.session.commit()
            except IntergityError:
                flash("Такой польхователь уже существует", "danger")
                return render_template('standard', form=form)
            else:
                flash("Вы успешно зарегистрировались", "success")
            return redirect(url_for('employee'))
        else:
            print(form.errors)
    return render_template('standart_form.html', form=form)






def employee_update(employee_id):
        employee = Employee.query.get(employee_id)
        form = EmployeeForm(obj=employee)
        if request.method == 'POST':
            if form.validate_on_submit():
                form.populate_obj(employee)
                db.session.add(employee)
                db.session.commit()
                return redirect(url_for('index'))
            else:
                print(form.errors)
        return render_template('standart_form.html', form=form)



def employee_delete(employee_id):
        employee = Employee.query.get(id)
        if request.method == "POST":
            db.session.delete(employee)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('comfirm_delete.html',employee_id=employee_id)



def register():
    title = 'Регистрация Работника'
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User()
            form.populate_obj(user)
            db.session.add(user)
            try:
                db.session.commit()
            except IntergityError:
                flash("Такой польхователь уже существует", "danger")
                return render_template('user_form.html', form=form, title=title)
            else:
                flash("Вы успешно зарегистрировались", "success")
            return redirect(url_for('login'), title=title)
        else:
            print(form.errors)
    return render_template('user_form.html', form=form)

def login():
    title = 'Login'
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                print('Errors data')
        else:
                print(form.errors)
        return render_template('user_form.html', form=form, title=title)


def logout():
    logout_user()
    return redirect(url_for('login'))

