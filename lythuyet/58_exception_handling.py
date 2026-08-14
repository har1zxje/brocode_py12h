try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("U stupid ass nigga")
except ValueError:
    print("Only enter number")
except Exception:
    print("Sth went wrong")
finally:
    print("Do some cleanup")