
#frequency of letters
def most_frequent(str):
    count={}
    for x in str:
        if x in count.keys():
            count[x]=count[x]+1
        else:
            count[x]=1
    sorted_count = sorted(count.items(), key=lambda x:x[1],reverse=True)
    dict_sorted_count=dict(sorted_count)
    print(dict_sorted_count)
a=input("Enter a string: ")
most_frequent(a)
