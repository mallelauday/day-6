num = int(input("Enter the no.of transactions"))
transaction = [0]*num
for i in range(num):
    transaction[i] = int(input('Enter amount:'))
categories={
    "normal":[],
    "larger":[],
    "high_risk":[],
    "invalid":[]
}
for i in transaction:
    if i<0:
        categories["invalid"].append(i)
    elif 1<=i<=500:
        categories["normal"].append(i)
    elif 500<=i<=2000:
        categories["larger"].append(i)
    else:
        categories["high_risk"].append(i)
valid=[t for t in transaction if(t>0)]
total_value=sum(valid)
num_transactions=len(transaction)
summary=(total_value,num_transactions)
frequent = num_transactions > 5
large_spending = total_value > 5000
suspicious = len(categories["high_risk"]) >= 3
if suspicious:
    risk = "High Risk"
elif large_spending or frequent:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"
print("Categorized Transactions:", categories)
print("Total Transaction Value:", total_value)
print("Number of Transactions:", num_transactions)
print("Summary Tuple:", summary)
print("Final Risk Classification:", risk)
if risk == "High Risk":
    print("High Risk detected")
elif risk == "Moderate Risk":
    print("Moderate Risk detected")
else:
    print('Low Risk detected')