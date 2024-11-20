# Part 4
d = pow(e,-1,f)

d_m_i = pow(e_m, d, x*y)

b = (d_m_i.bit_length() + 7)//8
d_m_b = d_m_i.to_bytes(b)
d_m = d_m_b.decode('utf-8')

print(f"decrypted int: {d_m_i}")
print(f"decrypted message: {d_m}")