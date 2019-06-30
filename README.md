## Description :-
http_r_code.py is python3 tool . it takes a list of subdomains and give you the response code for each subdomain and the output is three txt files 
1. file contain the subdomains with 2xx response code 
2. file contain the subdomains with 3xx response code
3. file contain the subdomains with 4xx response code
4. the unresolved or 5xx subdomains is not in the out put files it is only show in terminal 
## Instalation:-
1. git clone https://github.com/smackerdodi/http_r_code.git
2. cd http_r_code
3. pip3 install -r requirements 
## Usage-
python3 http_r_code.py subd.txt ./200.txt ./300.txt ./400.txt 
where:-
1. subd.txt : text file contains a list of subdomains in this format www.example.com (without http:// or https://)
2. 200.txt : text file contain the output of subdomains with response code 2xx
3. 300.txt : text file contain the output of subdomains with response code 3xx
4. 400.txt : text file contain the output of subdomains with response code 4xx
## Notes :-
1.  tool must take the four file as arguements or it will not work ( the first must exist but the other if it is not exist the tool will create it )
2. the output of the tool is coloures to make it easy for the eyes 
3. if the subdomain has 3xx response code which mean redirect the toll print out the location header which is the subdomain redirect to 
