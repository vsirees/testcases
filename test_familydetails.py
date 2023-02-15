import pytest

family={"family_member":["Bose", "Padma", "Arun", "lakshmi", "Ashok", "Sireesha", "Lochan", "Hitesh", "Candy", "Chinnu"]}

def test_family1():
    fathername=family["family_member"][0]
    assert fathername == "Bose", "Please give correct name of father"

def test_family2():
    mothername=family["family_member"][0]
    assert mothername == "Padma", "Please give correct name of mother"

def test_family3():
    brothername=family["family_member"][2]
    assert brothername == "Arun", "Please give correct name of brother"

def test_family4():
    milname=family["family_member"][3]
    assert milname == "Lakshmi", "Please give correct name of Mother in Law"

def test_family5():
    husname=family["family_member"][4]
    assert husname == "Ashok", "Please give correct name of husband"

def test_family6():
    myname=family["family_member"][5]
    assert myname == "Lochan", "Please give correct name"

def test_family7():
    sonname=family["family_member"][6]
    assert sonname == "Siresha", "Please give correct name of son"

def test_family8():
    nephew1name=family["family_member"][7]
    assert nephew1name == "Hitesh", "Please give correct name of nephew"

def test_family9():
    nephew2name=family["family_member"][8]
    assert nephew2name == "Candy", "Please give correct name of nephew"

def test_family10():
    nephew3name=family["family_member"][9]
    assert nephew3name == "Chinu", "Please give correct name of nephew"