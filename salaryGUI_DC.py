"""
Program: salaryGUI_DC.py
Author:  Dominick Chiofolo  7/19/2023

GUI-based program to calculate the salary of an employee
NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

"""

from breezypythongui import EasyFrame
from tkinter.font import Font
import random
# Other imports go here

# Class header (application name will change project to project)
class SalaryCalculator(EasyFrame):
	# Definition of our class constructor method
	def __init__(self):
		# Call to the Easy Frame constructor method
		EasyFrame.__init__(self, title = "Salary Calculator", width = 260, height = 320, background = "darkslategray", resizable = False)
		# Program title for the salary calculator label
		self.addLabel(text = "Salary Calculator", row = 0, column = 0, columnspan = 2, sticky = "NEW", font = Font(family = "Times New Roman, bold", size = 25), background = "darkslategray", foreground = "darkorange")

		# Input phase 
		self.addLabel(text = "Hourly Wage:", row = 2, column = 0, columnspan = 2, sticky = "NW", font = Font(family = "Times New Roman"), background = "darkslategray", foreground = "white")
		self.rate = self.addFloatField(value = 0.0, row = 2, column = 1, columnspan = 2)
		self.rate["width"] = 7
		self.addLabel(text = "Hours Worked:", row = 3, column = 0, columnspan = 2, sticky = "NW", font = Font(family = "Times New Roman"), background = "darkslategray", foreground = "white")
		self.hours = self.addFloatField(value = 0.0, row = 3, column = 1, columnspan = 2)
		self.hours["width"] = 7
		self.button = self.addButton(text = "Calculate", row = 4, column = 0, columnspan = 2, command = self.calculate)
		self.button["width"] = 15
		self.button["background"] = "darkorange"
		self.button["activebackground"] = "darkorange"
		self.button["font"] = "bold"

		# Output phase
		self.addLabel(text = "Total Salary:", row = 1, column = 0, columnspan = 2, sticky = "NW", font = Font(family = "Times New Roman", size = 20), background = "darkslategray", foreground = "white")
		self.salary = self.addFloatField(value = 0.0, row = 1, column = 1, columnspan = 2, state = "readonly", precision = 2)
		self.salary["width"] = 7

	def calculate(self):
		# Grab user input
		pay = self.rate.getNumber()
		hours = self.hours.getNumber()

		# Processing phase
		result = (pay * hours)

		# Output phase
		self.salary.setNumber(result)

# Global definition of the main() method
def main():
	# Instantiate an object from the class into mainloop()
	SalaryCalculator().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()