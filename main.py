# ErickWilfredLv6ICT
# Enjoy
Title = "\nthis is a small project showing how to \ninterconnect modules by import them"
print(Title.upper())
while True:
    print("\n================================= \n1.Factorial Method Checker\n2.Palindrome Method Checker\n3.Leap Year "
          "Checker\n4.Prime Number "
          "Checker\n5.Average Sample Checker "
          "\n6.Exit Program\n7.Shutdown Pc")
    choice = int(input("Select Now\n"))
    if choice == 1:
        import factorial

        module_1 = factorial.namba
    elif choice == 2:
        import palindromefinderString3

        module_2 = palindromefinderString3.word_to_be_checked
    elif choice == 3:
        import leapyear

        module_3 = leapyear.leapYear
    elif choice == 4:
        import primenumber

        module_4 = primenumber.num
    elif choice == 5:
        import marksgrading

        module_5 = marksgrading.math
    elif choice == 6:
        exit()
    elif choice == 7:
        import toshutdownOS

        module_6 = toshutdownOS.shutdown_pc()

    else:
        print("Please Follow Instruction")
