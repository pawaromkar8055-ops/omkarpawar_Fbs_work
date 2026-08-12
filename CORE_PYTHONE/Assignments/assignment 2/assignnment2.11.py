#number of notes present in a given amount
amount=int(input("enter the amount:"))
no500=amount//500
amount=amount%500
no200=amount//200
amount=amount%200
no100=amount//100
amount=amount%100
no50=amount//50
amount=amount%50
no20=amount//20
amount=amount%20
no10=amount//10
amounnt=amount%10
no5=amount//5
amount=amount%5
no2=amount//2
amount=amount%2
no1=amount//1
print(f" 500 notes: {no500}, 200 notes: {no200}, 100 notes: {no100}, 50 notes: {no50}, 20 notes: {no20}, 10 notes: {no10}, 5 notes: {no5}, 2 notes: {no2}, 1 notes: {no1}")