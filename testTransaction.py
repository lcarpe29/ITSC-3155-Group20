import pytest
from transaction import Transaction

@pytest.fixture()
def transaction():
    transaction = Transaction("4/20/20", "Deposit", 100, -1)
    return transaction

def test_getID(transaction):
    assert transaction.get_id() == -1

def test_getDate(transaction):
    assert transaction.get_date() == "4/20/20"

def test_getType(transaction):
    assert transaction.get_type() == "Deposit"

def test_getAmount(transaction):
    assert transaction.get_amount() == 100

def test_recordTransaction(transaction):
    assert transaction.record_transaction() == True

def test_toString(transaction):
    testDisplay = "Date: " + "4/20/20" + "\tType: " + "Deposit" + "\tAmount: " + str(100)
    assert transaction.to_string() == testDisplay
