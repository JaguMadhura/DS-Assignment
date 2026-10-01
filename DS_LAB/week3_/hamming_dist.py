def hamming_dist(str1, str2):
    if len(str1) != len(str2):
       raise ValueError("Strings must be of equal length")

    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))
s1="I am Madhu"
s2="I an datas"

dist=hamming_dist(s1,s2)
print(f"Hamming distance between '{s1}' and '{s2}' : {dist}")
