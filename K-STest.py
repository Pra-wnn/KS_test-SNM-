alp = 0.05

N = int(input("Enter number of random number: "))
randn = []


for i in range(N):
    value = float(input("Enter random number: "))
    randn.append(value)

randn.append(0.000)



randnn = sorted(randn, key = lambda x:float(x))

print(randnn[0])

for i in range(1,N+1):
    sd = i/N
    print("i/N:",sd," || ","(i/N) - R ",sd-randnn[i]," || ","R -(i-1)/N)",randnn[i]- ((i-1)/N))