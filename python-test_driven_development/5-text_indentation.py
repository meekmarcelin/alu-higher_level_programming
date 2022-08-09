#!/usr/bin/python3
""" print a text """


def text_indentation(text):
    """ text indentation """
    if type(text) != str:
        raise TypeError('text must be a string')
    sentence = (':' + '\n\n').join([x.strip(" ") for x in text.split(':')])
    sentence = ('.' + '\n\n').join([y.strip(" ") for y in sentence.split('.')])
    sentence = ('?' + '\n\n').join([z.strip(" ") for z in sentence.split('?')])
    print(sentence, end="")
