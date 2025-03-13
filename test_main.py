from main import get_weather, add, divide, UserManager, is_prime
import pytest

@pytest.fixture
def user_manager():
    """Creates a fresh instance of UserManager before each test."""
    return UserManager()

# runs usermanager function and gives us new UserManager instance
def test_add_user(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com") == True # added a user
    assert user_manager.get_user("john_doe") == "john@example.com" # user key should be equal to the user email

# runs usermanager function and gives us new UserManager instance
def test_add_duplicate_user(user_manager):
    user_manager.add_user("john_doe", "john@example.com") # added a user
    with pytest.raises(ValueError):
        user_manager.add_user("john_doe", "another@example.com") # adding with existing username should throw Value error


def test_get_weather():
    assert get_weather(21) == "hot" # condition needs to be true to pass
    assert get_weather(10) == "cold" 
    assert get_weather(30) == "hot"

    
def test_add():
    assert add(2, 3) == 5, "2 + 3 should be 5"
    assert add(-1, 1) == 0, " -1 + 1 should be 0"
    assert add(0, 0) == 0, "0 + 0 should be 0"

def test_divide():
    with pytest.raises(ValueError, match = "Cannot divide by zero"):
        divide(10, 0)

@pytest.mark.parametrize("num, expected", [
    (1, False), 
    (2, True), 
    (3, True),
    (4, False),
    (17, True),
])
def test_is_prime(num, expected):
    assert is_prime(num) == expected