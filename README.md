# day-6
1️ Algorithm Explanation:
First, I take the number of transactions as input and store the values in a list using a loop. Then, I classify each transaction into categories (invalid, normal, large, high risk) using conditional statements and store them in a dictionary. I use list comprehension to filter valid transactions and calculate the total value. After that, I check patterns like number of transactions, total amount, and count of high-risk transactions. Based on these conditions, I determine the final risk level. Finally, I display the categorized data, summary, and risk classification.
2️ Additional Test Cases
Test Case 1
Enter the no.of transactions3
Enter amount:12
Enter amount:123
Enter amount:125
Categorized Transactions: {'normal': [12, 123, 125], 'larger': [], 'high_risk': [], 'invalid': []}
Total Transaction Value: 260
Number of Transactions: 3
Summary Tuple: (260, 3)
Final Risk Classification: Low Risk
Low Risk detected
Test Case 2
Enter the no.of transactions2
Enter amount:12
Enter amount:47526
Categorized Transactions: {'normal': [12], 'larger': [], 'high_risk': [47526], 'invalid': []}
Total Transaction Value: 47538
Number of Transactions: 2
Summary Tuple: (47538, 2)
Final Risk Classification: Moderate Risk
Moderate Risk detected
3️. Reflection:
One logic decision I made was to prioritize suspicious patterns such as multiple high-risk transactions while determining the final risk. This ensures that even if other conditions are normal, repeated high-risk activities are treated as a serious issue.
