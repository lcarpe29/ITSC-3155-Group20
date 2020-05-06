import pytest
from user import User
from transaction import Transaction


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


def test_getFirstName(user):
    assert user.get_firstname() == "Norm"


def test_getLastName(user):
    assert user.get_lastname() == "Niner"


def test_getPassword(user):
    assert user.get_password() == "Password"


def test_getBalance(user):
    assert user.get_balance() == 80


def test_getAccoundID(user):
    assert user.get_accountid() == 2


def test_getUserLog(user):
    userLog = [
        Transaction("4/20/20", "Deposit", 100, 2),
        Transaction("4/22/20", "Withdraw", 20, 2)
    ]
    for x in range(2):
        assert user.get_userlog()[x].to_string() == userLog[x].to_string()


def test_setBalance(user):
    assert user.get_balance() == 80
    user.set_balance(100)
    assert user.get_balance() == 100

def test_createLog(user, log):
    assert user.get_userlog() != log
    assert user.get_userlog() == user.create_log(log)
