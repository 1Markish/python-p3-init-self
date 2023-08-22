#!/usr/bin/env python3

class Dog:
    def __init__(self, name , breed ="Mutt"):
        self.name = name
        self.breed = breed
    def test_saves_self_breed(self , breed) : 
        self.breed = breed
        