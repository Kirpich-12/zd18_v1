input_data = open('input.txt', 'r')
data = input_data.read()
fact = int(data)

ans = 1
 
for i in  range(1, fact + 1):
    ans *= i

output_data = open('output.txt', 'w')
output_data.write(str(ans))

input_data.close()
output_data.close()