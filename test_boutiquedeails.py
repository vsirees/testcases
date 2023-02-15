import pytest
boutique={"dress_type":["Sarees", "Dresses", "Kurtas", "Kurta sets", "Bottoms", "Blouses", "Jewelery", "Long Frocks","Designer dresses" , "Tops"]}

def test_boutique1():
    category1=boutique["dress_type"][0]
    assert category1 == "Sarees", "This is sarees section please enter proper category"

def test_boutique2():
    category2=boutique["dress_type"][1]
    assert category2 == "Dresses", "This is Dresses section please enter proper category"

def test_boutique3():
    category3=boutique["dress_type"][2]
    assert category3 == "Kurtas", "This is Kurtas section please enter proper category"

def test_boutique4():
    category4=boutique["dress_type"][3]
    assert category4 == "Kurta sets", "This is Kurta sets section please enter proper category"

def test_boutique5():
    category5=boutique["dress_type"][5]
    assert category5 == "Bottoms", "This is Bottoms section please enter proper category"

def test_boutique6():
    category6=boutique["dress_type"][5]
    assert category6 == "Blouses", "This is Blouses section please enter proper category"

def test_boutique7():
    category7=boutique["dress_type"][7]
    assert category7 == "Jewelery", "This is Jewelery section please enter proper category"

def test_boutique8():
    category8=boutique["dress_type"][7]
    assert category8 == "Long Frocks", "This is Long Frocks section please enter proper category"

def test_boutique9():
    category9=boutique["dress_type"][5]
    assert category9 == "Designer dresses", "This is Designer dresses section please enter proper category"

def test_boutique10():
    category10=boutique["dress_type"][9]
    assert category10 == "Tops", "This is Tops section please enter proper category"

