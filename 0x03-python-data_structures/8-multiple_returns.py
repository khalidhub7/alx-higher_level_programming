#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        new_sen = None + sentence[1:]
        length = len(new_sen)
        first = new_sen[0]
    elif len(sentence) > 0:
        length = len(sentence)
        first = sentence[0]
        return length, first
