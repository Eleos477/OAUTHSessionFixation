#Taken from old demo. Need to put other objects here once they're importing correctly
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField, SubmitField
from flask import flash
from random import seed
from random import randint

class User():
    def __init__(self, accountNum, name, surname, password):
        self.name = name
        self.surname = surname
        self.password = password
        self.accountNum = accountNum # For convenience
        self.account = Account(self.accountNum)

    def deposit(self, deposit):
        if (deposit > 0):
            self.account.balance += deposit

    def withdraw(self, withdrawal):
        if (withdrawal > 0):
            if (self.account.balance - withdrawal >= 0):
                self.account.balance -= withdrawal

    def checkBalance(self):
        print("\nAccount Number:",self.account.accountNum)
        print("Account Balance: $",self.account.balance)

        return None

class Account():
    def __init__(self, accountNum):
        self.accountNum = accountNum
        self.balance = 1000000

class Session():
    def __init__(self, ID, accountNum):
        self.ID = ID
        self.accountNum = accountNum


#############
### FORMS ###
#############
class RegistrationForm(Form):
    fname = StringField('First name: ', [validators.DataRequired()])
    lname = StringField('Last name: ', [validators.DataRequired()])
    password = PasswordField('Password:', [validators.DataRequired()])

class LoginForm(Form):
    accountNum = IntegerField('Account Number: ', [validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired()])

class TransactionForm(Form):
    amount = IntegerField('Transaction Amount ($): ', [validators.DataRequired()])
    deposit = SubmitField(label='Deposit')
    withdraw = SubmitField(label='Withdraw')