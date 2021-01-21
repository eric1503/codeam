from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window 

# Set app size
Window.size = (500,700)

#Designate kv file
Builder.load_file('calculatorkivy.kv')

class MyLayout(Widget):
	def clear(self):
		self.ids.calc_input.text = '0'

	def remove(self):
		prior = self.ids.calc_input.text
		# Removing last item
		prior = prior[:-1]
		#Output in the text box
		self.ids.calc_input.text = prior

	def button_press(self, button):
		#Create variable that contains whatever in the textbox
		prior = self.ids.calc_input.text

		#Test for error
		if "Error" in prior:
			prior = ''

		#determine if0 is sitting there
		if prior == "0":
			self.ids.calc_input.text = ''
			self.ids.calc_input.text = f'{button}'
		else:
			self.ids.calc_input.text = f'{prior}{button}'

	def dot(self):
		prior = self.ids.calc_input.text
		num_list = prior.split("+")

		if "+" in prior and "." not in num_list[-1]:
			prior = f'{prior}.'
			self.ids.calc_input.text = prior

		elif "." in prior:
			pass

		else:
			prior = f'{prior}.'
			self.ids.calc_input.text = prior

	def pos_neg(self):
		prior = self.ids.calc_input.text
		if "-" in prior:
			self.ids.calc_input.text = f'{prior.replace("-", "")}'
		else:
			self.ids.calc_input.text = f'-{prior}'

	def math_sign(self, sign):
		prior = self.ids.calc_input.text
		self.ids.calc_input.text = f'{prior}{sign}'

	def equal(self):
		prior = self.ids.calc_input.text
		#Error Handling
		try:
			#Evaluate the math
			answer = eval(prior)
			#Output the answer
			self.ids.calc_input.text = str(answer)
		except:
			self.ids.calc_input.text = "Error"


		#if "+" in prior:
			#num_list = prior.split("+")
			#answer = 0.0
			#loop
			#for number in num_list:
				#answer = answer + float(number)

			#print answer in text box
			#self.ids.calc_input.text = str(answer)

		#if "-" in prior:
			#pass






class CalculatorApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	CalculatorApp().run()