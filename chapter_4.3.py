message = (input("Enter a message: "))
message_length = len(message)

message_backwards = ""

for i in range(message_length):
  # print(i)
  # print(message_length - i - 1)

  # print(message[i])
  # print(message[message_length - i - 1])

  message_backwards += message[message_length - i - 1]

print(message)
print(message_backwards)