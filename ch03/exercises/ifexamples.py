def main():

    integ = int(input("ENTER A NUMBER TO SEE IF ITS EVEN OR ODD: "))
    grade = int(input("ENTER A GRADE TO SEE IF IT PASSES: "))
    tempr = int(input("ENTER A TEMPERATURE TO SEE IF ITS HOT OR COLD: "))
    age = int(input("ENTER AN AGE TO SEE IF YOU'RE LEGAL: "))
    posor = int(input("ENTER AN INTEGER TO SEE IF ITS POSITIVE AND ODD OR EVEN: "))

    if (integ % 2 == 1):
        print("ODD")
    else:
        print("EVEN")

    if grade >= 60:
        print("PASS")
    else:
        print("FAIL")

    if tempr > 80:
        print("HOT")
    elif tempr > 50:
        print("WARM")
    else:
        print("COLD")

    if age >= 18:
        print("DON'T NEED ID")
    else:
        print("NEED ID")

    if posor < 0:
        print("NEGATORY")
    elif (posor % 2 == 1):
        print("POSITIVE AND ODD")
    else:
        print("POSITIVE AND EVEN")

main()