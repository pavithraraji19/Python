altitude=int(input("enter the altitude:"))
if altitude<=1000 :
    print("hi pilot! Its 1000 altitude ,u can land the plane")
elif altitude>1000 and altitude<5000 :
    print("hi pilot ,its more than 1000 and less thsn 5000 so, you come down to 1000 ft")
else:
     print("hi pilot ,its more than 5000 so ,go around and try later")
