def find_primitive(n):
    for r in range(1, n):
        li = []
        for x in range(n - 1):
            val = pow(r, x, n)
            if val in li:
                break
            li.append(val)
        else:
            return r



q = int(input("Enter a prime number q: "))
a = find_primitive(q)
a_private = int(input("Enter private key of A: "))
a_public = pow(a, a_private, q)
b_private = int(input("Enter private key of B: "))
b_public = pow(a, b_private, q)

a_secret = pow(b_public, a_private, q)
b_secret = pow(a_public, b_private, q)
print("###################################")
print("The public key value by YA is:", a_public)
print("The public key value by YB is:", b_public)
print("-----------------------------------")
print("The key value generated by KA is:", a_secret)
print("The key value generated by KB is:", b_secret)
print("###################################")
