# Name: Collins Ramsey
# morse_code.py
#
# Purpose: Encodes a message into Morse Code
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.
from graphics import *


def morse_code():
    # create window
    width = 500
    height = 400
    win = GraphWin("Morse Code", width, height)

    # make interesting background
    background = Image(Point(width / 2, height / 2), "matrix.gif")
    background.draw(win)

    # display to user what to input
    msg_box = Text(Point(100, 50), "Message to code")
    msg_box.setFill('white')
    msg_box_2 = Rectangle(Point(30, 40), Point(170, 60))
    msg_box_2.setFill('black')
    msg_box_2.draw(win)
    msg_box.draw(win)

    # create input box
    real_msg = Entry(Point(280, 50), 20)
    real_msg.draw(win)

    # make encode button
    button = Text(Point(width / 2, height / 2), "Encode")
    button.setTextColor('white')
    border = Rectangle(Point(width / 2 - 35, height / 2 - 20),
                       Point(width / 2 + 35, height / 2 + 20))
    border.setOutline('white')
    border.draw(win)
    button.draw(win)

    # wait for click to encode
    win.getMouse()

    # take message and convert it to morse code
    # remove encode button and border
    border.undraw()
    button.undraw()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    lst = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
           ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
           "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "   "]
    encoded_msg = real_msg.getText().upper()
    output_lst = []
    for i in range(len(encoded_msg)):
        letter = alpha.find(encoded_msg[i])
        output_lst.append(lst[letter])
    final = " ".join(output_lst)
    output_msg = Text(Point(250, 200), final)
    output_msg.setTextColor('white')
    output_msg.setSize(25)
    result_msg = Text(Point(250, 180), "Resulting Message")
    result_msg.setTextColor('white')
    result_msg.draw(win)
    output_msg.draw(win)

    # tell user to click anywhere and wait for click
    end = Text(Point(250, 300), "Click anywhere to close")
    end.setTextColor('white')
    end.draw(win)
    win.getMouse()
    win.close()


morse_code()
