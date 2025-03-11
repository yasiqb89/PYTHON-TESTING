from main import get_weather

def test_get_weather():
    assert get_weather(21) == "hot" # condition needs to be true to pass

    
