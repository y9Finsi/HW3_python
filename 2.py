num_bits = int(input())
binary_str = '0'
while len(binary_str) < num_bits:
    complement_str = ''.join(['0' if char == '1' else '1' for char in binary_str])
    binary_str += complement_str[:num_bits-len(binary_str)]
print(binary_str[:num_bits])


 #код не полностью успел допсать до назначенной даты, но всетаки вот фулл
