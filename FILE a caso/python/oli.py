enc = "f{anuiraaso_lfltnfi_sin_aime_rotpze_gne_ca_roi}_"

n = len(enc)//4
cols = [enc[n*i:n*(i+1)] for i in range(4)]

flag = ""
for i in range(n):
    flag += "".join(col[i] for col in cols)
print(flag)