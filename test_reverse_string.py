from reverse_string import reverse_text

def test_reverse():
    assert reverse_text("hello") == "olleh"
    assert reverse_text("madam") == "madam"
    
    print("Test case passed")
