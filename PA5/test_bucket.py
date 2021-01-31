from bucket import *
import pytest

def test_add():
    b = Bucket()
    b.insert("Kristofer", "er bestur")
    assert b["Kristofer"] == "er bestur"

def test_add_already_exists():
    b = Bucket()
    b.insert("Kristofer", "er bestur")
    with pytest.raises(ItemExistsException):
        b.insert("Kristofer", "er svakalegur")

def test_update_in():
    b = Bucket()
    b.insert(1, "einn")
    b.update(1, "asinn")
    assert b[1] == "asinn"

def test_update_not_in():
    b = Bucket()
    with pytest.raises(NotFoundException):
        b.update(1, "einn")
    
def test_contains():
    b = Bucket()
    b.insert(1, "einn")
    assert b.contains(1) == True
    assert b.contains(2) == False

def test_remove():
    b = Bucket()
    b.insert(1, "einn")
    b.insert(2, "tveir")
    b.remove(1)
    with  pytest.raises(NotFoundException):
        b.find(1)

def test_set_item():
    b = Bucket()
    b[1] = "einn"
    assert b[1] == "einn"
    b[1] = "as"
    assert b[1] == "as"

def test_get_item():
    b = Bucket()
    b[1] = "einn"
    b[2] = "tveir"
    assert b[1] == "einn"
    assert b[2] == "tveir"

def test_len():
    b = Bucket()
    b[1] = "einn"
    b[2] = "tveir"
    assert len(b) == 2
    b.remove(1)
    assert len(b) == 1
    b.remove(2)
    assert len(b) == 0