sequence_1 = str(input("Введите последовательность неотрицательных чисел через пробел: "))

for i in range(len(sequence_1)):
   if sequence_1[0] == '.':
      sequence_1[0] == ''
   elif sequence_1[len(sequence_1)] == '.':
      sequence_1[len(sequence_1)] == ''

print(sequence_1)

def change_dots(sequence_1):
   if '..' not in sequence_1:
      return sequence_1

   for i in range(1, len(sequence_1)):
      if str(sequence_1[i-1] + sequence_1[i]) == '..':
         a = sequence_1.replace((sequence_1[i-1] + sequence_1[i]), sequence_1[i])
         #a = sequence_1.replace('..', '.')
         a = sequence_1
         return change_dots(sequence_1)
         #if str(sequence_1[i-1] + sequence_1[i]) != '..':
            #break

b = change_dots(sequence_1)
print(b)
