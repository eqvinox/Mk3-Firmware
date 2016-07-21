### Author: EMF Badge team
### Description: Some basic UGFX powered dialogs
### License: MIT

import ugfx
import buttons
import pyb

def notice(text, close_text="Close", width = 213, height = 120):
	prompt_boolean(text, true_text = close_text, false_text = None, width = width, height = height)

def prompt_boolean(text, true_text="Yes", false_text="No", width = 213, height = 120):
	"""A simple one and two-options dialog

	if 'false_text' is set to None only one button is displayed.
	If both 'true_text' and 'false_text' are given a boolean is returned
	"""
	window = ugfx.Container(int(ugfx.width()/6), int(ugfx.height()/4), width, height)

	if false_text:
		true_text = "A: " + true_text
		false_text = "B: " + false_text

	button_yes = ugfx.Button(int(width/12), int(height*3/5), int(width/3), int(height/5), true_text, parent=window)
	button_no = ugfx.Button(int(width/2 + width/12), int(height*3/5), int(width/3), int(height/5), false_text, parent=window) if false_text else None
	label = ugfx.Label(int(width/10), int(height/10), int(width*4/5), int(height*2/5), text, parent=window)

	try:
		buttons.init()

		button_yes.attach_input(ugfx.BTN_A,0)
		if button_no: button_no.attach_input(ugfx.BTN_B,0)

		window.show()

		while True:
			pyb.wfi()
			if buttons.is_triggered("BTN_A"): return True
			if buttons.is_triggered("BTN_B"): return False

	finally:
		window.hide()
		window.destroy()
		button_yes.destroy()
		if button_no: button_no.destroy()
		label.destroy()

def prompt_text(description, default="", init_text = "", true_text="OK", false_text="Back", width = 300, height = 200):
	"""Shows a dialog and keyboard that allows the user to input/change a string"""
	"""A simple one and two-options dialog

	if 'false_text' is set to None only one button is displayed.
	If both 'true_text' and 'false_text' are given a boolean is returned
	"""
	window = ugfx.Container(int((ugfx.width()-width)/2), int((ugfx.height()-height)/2), width, height)

	if false_text:
		true_text = "A: " + true_text
		false_text = "B: " + false_text
		
	kb = ugfx.Keyboard(0, int(height/2), width, int(height/2), parent=window)
	edit = ugfx.Textbox(5, int(height/2)-30, int(width*4/5)-10, 25, text = init_text, parent=window)
	button_yes = ugfx.Button(int(width*4/5), int(height/2)-30, int(width*1/5)-3, 25 , true_text, parent=window)
	button_no = ugfx.Button(int(width*4/5), int(height/2)-30-30, int(width/5)-3, 25 , false_text, parent=window) if false_text else None
	label = ugfx.Label(int(width/10), int(height/10), int(width*4/5), int(height*2/5)-60, description, parent=window)
		
	
	try:
		buttons.init()

		button_yes.attach_input(ugfx.BTN_A,0)
		if button_no: button_no.attach_input(ugfx.BTN_B,0)

		window.show()

		while True:
			pyb.wfi()
			if buttons.is_triggered("BTN_A"): return edit.text()
			if buttons.is_triggered("BTN_B"): return default

	finally:
		window.hide()
		window.destroy()
		button_yes.destroy()
		if button_no: button_no.destroy()
		label.destroy()
		kb.destroy()
		edit.destroy();
	return default
