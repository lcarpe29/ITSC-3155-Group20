import pytest
from admin import Admin
from user import User
from transaction import Transaction


@pytest.fixture()
def admin():
    admin = Admin("admin", "test", "adminpassword", 1)
    return admin


@pytest.fixture()
def log():
    t1 = Transaction("4/20/20", "Deposit", 100, 2)
    t2 = Transaction("4/21/20", "Withdraw", 400, 3)
    t3 = Transaction("4/22/20", "Withdraw", 20, 2)
    log = [t1, t2, t3]
    return log


@pytest.fixture()
def user(log):
    user = User("Norm", "Niner", "Password", 80, 2, log)
    return user


@pytest.fixture()
def amount():
    amount = 25
    return amount


def test_getFirstName(admin):
    assert admin.get_firstname() == "admin"


def test_getLastName(admin):
    assert admin.get_lastname() == "test"


def test_getPassword(admin):
    assert admin.get_password() == "adminpassword"


def test_getAccountID(admin):
    assert admin.get_accountid() == 1


def test_userWithdraw(admin, user, amount):
    assert user.get_balance() == 80
    admin.user_withdraw(user, amount)
    assert user.get_balance() == 55


def test_userDeposit(admin, user, amount):
    assert user.get_balance() == 80
    admin.user_deposit(user, amount)
    assert user.get_balance() == 105
