#import function
import wolframalpha
#input from user
question = input("Question:")
app_id = 'WAPQ86-36Q7U9RXAJ'
client = wolframalpha.Client(app_id)
res = client.query(question)
answer = next(res.results).text
print(answer)
    
