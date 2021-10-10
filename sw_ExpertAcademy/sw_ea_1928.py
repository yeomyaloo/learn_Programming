import base64

t = int(input())

for tc in range(1,t+1):
    s = input()
    enc = s.encode("UTF-8")
    dec = base64.b64decode(enc)

    print(f'#{tc} {dec.decode("UTF-8")}')
