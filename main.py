import requests
def request(url):
   try:
     result = requests.get("https://" + url)
     if(result):
        print("[+] Subdomain discovered -------> " + url)
   except:
      pass

def main():
    target_url = input("Enter the domain name to scan for subdomain ")
    #open subd list
    with open("d:\project\Subdomain enumeration\subdmainwordlist.txt", "r") as wordlist:
        for line in wordlist:
         word = line.strip()
         print(word)
         test_url = word + "." + target_url
         request(test_url)

main()    