#!/usr/bin/env python3

def init_globals():
    global GLOBALS
    GLOBALS = {}

def set(name, value)-> bool:
    try:
        GLOBALS[name] = value
        return True
    except KeyError:
        return False

def get(name) -> str:
    try:
        return GLOBALS[name]
    except KeyError:
        return "Not Found"

def delete(name) -> bool:
    try:
        del GLOBALS[name]
        return True
    except KeyError:
        return False
