grt = input("Greeting: ").lstrip()
#new_grt = grt.lower()

if (grt[0:5]).lower() == "hello":
    print("$0")

#if 'hello' in new_grt:
    #print("$0")

elif (grt[0]).lower() == "h":
    print("$20")

#elif 'h' in new_grt[0]:
    #print("$20")

else:
    print("$100")