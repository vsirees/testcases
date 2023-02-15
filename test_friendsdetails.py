import pytest

friends={"friend_names":["Uma", "Anjali", "Kavitha", "Manjula", "Vennela", "Ram", "Sai", "Anil","Srikar","Raghu"]}

def test_friends1():
    girlname1=friends["friend_names"][0]
    assert girlname1 == "Uma", "Please give a girl name"

def test_friends2():
    girlname2=friends["friend_names"][1]
    assert girlname2 == "Sai", "Please give a girl name"

def test_friends3():
    girlname3=friends["friend_names"][2]
    assert girlname3 == "Kavitha", "Please give a girl name"

def test_friends4():
    girlname4=friends["friend_names"][3]
    assert girlname4 == "Ram", "Please give a girl name"

def test_friends5():
    girlname5=friends["friend_names"][4]
    assert girlname5 == "Raghu", "Please give a boy name"

def test_friends6():
    boyname1=friends["friend_names"][5]
    assert boyname1 == "Anjali", "Please give a boy name"

def test_friends7():
    boyname2=friends["friend_names"][6]
    assert boyname2 == "Vennela", "Please give a boy name"

def test_friends8():
    boyname3=friends["friend_names"][7]
    assert boyname3 == "Anil", "Please give a boy name"

def test_friends9():
    boyname4=friends["friend_names"][8]
    assert boyname4 == "Srikar", "Please give a boy name"

def test_friends10():
    boyname5=friends["friend_names"][9]
    assert boyname5 == "Manjula", "Please give a boy name"
    