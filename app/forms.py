from flask_wtf import FlaskForm
import wtforms as wf

from . import app
from .models import Position, Employee, User


def get_positiion():
    with app.app_context():
        positions = Position.query.all()
        choices = []
        for position in positions:
            choices.append((position.id, position.name))
        return choices



class PositionForm(FlaskForm):
    name = wf.StringField(label='Название позиции')
    department = wf.StringField(label='Отделение')
    wage = wf.IntegerField(label='Зарплата')


class EmployeeForm(FlaskForm):
    name = wf.StringField(label='Имя сотрудника')
    inn = wf.StringField(label='ИНН сотрудника')
    position_id = wf.SelectField(label='Должность ', choices=[])

    def validate_inn(self, field):
        if not field.data[1:].startwith(1, 2):
            raise wf.validators.ValidationError('Имя не должно быть больше 2')



def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position_id.choices = get_positiion()



class UserForm(FlaskForm):
    username = wf.StringField(label='Login', validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=8, max=24)
    ])
    password = wf.PasswordField(label='Password', validators=[
        wf.validators.DataRequired(),
    ])

    def validate_password(self, field):
        if field.data.insdigit() or field.data.isalpha():
            raise wf.validators.ValidationError('Пароль должен содержать числа и буквы')

