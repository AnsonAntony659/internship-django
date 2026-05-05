def main():
    a=[42,29,74,11,65,58]
    n=len(a)
    print("original list:",a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                print("List after sorting is:",a)
main()
