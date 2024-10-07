from math import factorial as fact

input_data = open('input.txt', 'r')
data = input_data.read()
n = int(data)

ans = fact(n)

output_data = open('output.txt', 'w')
output_data.write(str(ans))

input_data.close()
output_data.close()