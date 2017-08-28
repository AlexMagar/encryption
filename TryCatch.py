while True:
	try:
		number = int(input("Entre a number:"))
		print(18/number)
		break
	except ValueError:
		print("You entre string please entre number")
	except ZeroDivisionError:
		print("please entre number grater than 0")
		break
	finally:
		print("Thank You!")