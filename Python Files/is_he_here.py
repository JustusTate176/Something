print("==============================")
print("       Is He Here")
print("==============================")

is_he_here = input("Is he here yet? (Y/N): ").lower()

if is_he_here == "y":
    does_he_know = input("Does he know you're here? (Y/N): ").lower()

    if does_he_know == "y":
        action = "RUN"
        print("\nRUN AS FAST AS YOU CAN.")

    elif does_he_know == "n":
        action = "HIDE"
        print("\nGET OUT OF THERE NOW.")

    else:
        action = "WAIT"
        print("\nYou are not sure what to do. Stay quiet.")

elif is_he_here == "n":
    action = "SAFE"
    print("\nYou're safe... for now.")

else:
    action = "UNKNOWN"
    print("\nInvalid response.")

print("\nYour next action:", action)
print("==============================")




	