a = int(input("Enter the value : "))
for i in range(1, a + 1): # outer loop
    for j in range(1, i + 1): # inner loop
        print(j, end=" ")
    print('')