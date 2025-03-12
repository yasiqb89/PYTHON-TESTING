import pytest
from db import Database

@pytest.fixture
def db():
    database = Database()
    yield database #provide fixture instance : Setup operation
    database.data.clear() #cleanup step : Teardown operation 

def test_add_user(db):
    db.add_user(1, "Alice")
    assert db.get_user(1) == "Alice"

def test_add_duplicate_user(db):
    db.add_user(1, "Alice")
    with pytest.raises(ValueError, match = "User already exists"): 
        db.add_user(1, "Bob") #user_id 1 already added so shuould give User already exists 

def test_delete_user(db):
    db.add_user(2, "Bob")
    db.delete_user(2)
    assert db.get_user(2) is None 