'''
Using urllib, you can treat a web page much like a file. You simply indicate
which web page you would like to retrieve and urllib handles all of the HTTP
protocol and header details.

When the program runs, we only see the output of the contents of the file. The
headers are still sent, but the urllib code consumes the headers and only returns
the data to us.

As an example, we can write a program to retrieve the data for romeo.txt and
compute the frequency of each word in the file as follows:
'''
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

'''
Again, once we have opened the web page, we can read it like a local file.
'''