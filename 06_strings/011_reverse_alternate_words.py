words=input("Sentence:").split()
print(" ".join(w if i%2==0 else w[::-1] for i,w in enumerate(words)))
