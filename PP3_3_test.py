import os.path
import sys
import PP3_3

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP3_3.py")
		assert exists
	except:
		sys.exit()

	input_values = ['5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_3.input = mock_input

	PP3_3.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: 024\n"

def test_q2_1(capsys):

	try:
		exists = os.path.exists("PP3_3.py")
		assert exists
	except:
		sys.exit()

	input_values = ['7']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_3.input = mock_input

	PP3_3.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: 6543210\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP3_3.py")
		assert exists
	except:
		sys.exit()

	input_values = ['10']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_3.input = mock_input

	PP3_3.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: 0246810\n"

def test_q2_2(capsys):

	try:
		exists = os.path.exists("PP3_3.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-2', '12']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_3.input = mock_input

	PP3_3.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: In: 11109876543210\n"

def test_q1_3(capsys):

	try:
		exists = os.path.exists("PP3_3.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-10', '-5', '8']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_3.input = mock_input

	PP3_3.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In: In: 02468\n"

def test_q2_3(capsys):

	try:
		exists = os.path.exists("PP3_3.py")
		assert exists
	except:
		sys.exit()

	input_values = ['20']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_3.input = mock_input

	PP3_3.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: 191817161514131211109876543210\n"

