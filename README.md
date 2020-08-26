## Description :-
http_r_code.py is python3 tool . it takes a list of subdomains and give you the response code for each subdomain and the output is one text file contain all subdomain have response code 2xx or 3xx or 4xx or 5xx and if you want to grep 2xx subdomains you could use grep command as shown below 
1- cat response_code.txt | grep ' : [20.]' | tee -a 200.txt
2- cat response_code.txt | grep ' : [30.]' | tee -a 300.txt
3- cat response_code.txt | grep ' : [40.]' | tee -a 400.txt
 
## Instalation:-
1. git clone https://github.com/smackerdodi/http_r_code.git
2. cd http_r_code
3. pip3 install -r requirements 
## Usage-
python3 http_r_code.py subd.txt ./response_code.txt 
where:-
1. subd.txt : text file contains a list of subdomains in this format www.example.com (without http:// or https://)
2. response_code.txt file contain all subdomain have response code and you could filter it as shown above 
## Notes :-
1.  tool must take the two files as arguements or it will not work ( the first must exist but the other if it is not exist the tool will create it )

2. the output of the tool is coloures to make it easy for the eyes 

3. if the subdomain has 3xx response code which mean redirect the tool print out the location header which is the subdomain redirect to

4- now the tool is multi-threaded which mean it is so fast and you could increase or decrease the speed of the tool in the source code at (max_workers=40) you could change this number up or down depending on your computer resources or internet speed 
