from urllib.request import urlopen
import os
url = "http://www.cse.hcmut.edu.vn/~hiep/SlideOOP/ThuchanhOOP_New/"
html = urlopen(url)
cmp_str = "<a href="
lst_file = []
for line in html:
   line_str = line.decode('ascii')
   if all(isinstance(e, str) and e in line_str for e in [cmp_str,".pdf"]):
       lst_file.append(line_str[line_str.index(cmp_str)+len(cmp_str)+1:line_str.index(".pdf")+4])

lst_file_1 = list(map(lambda x: x.replace("%20","_") if ("%20" in x) else x,lst_file) )


os.chdir("C:/Users/Sang/Desktop/OOP")
for i,file in enumerate(lst_file):
    f = open(lst_file_1[i],'wb')
    f.write(urlopen(url+file).read())    

print("Download File Success Full")
