# Exercise 2

How to run the client and server.

From the `src` folder, run the server:

```bash
python -m rates_demo.rates_api
```

From the `src` folder, run the client:

```bash
python -m rates_demo 
```

1. Implement this code in `__main__.py` in the `rates_demo` folder. 

2. Install the "requests" package from PyPi.org.

https://docs.python-requests.org/en/master/user/quickstart/#make-a-request

3. Using the "requests" package API, call the following URL for each date returned from the "business_days" function. Copy the function from the "date_demos" folder, and utilize in the "rates_demo" folder.

http://127.0.0.1:5000/api/2019-01-01?base=USD&symbols=EUR

Specify a start date and then iterate over the next 20 days, and for each business in the 20 days, get the rate information from the rates API.

4. Create a list of text values from each response. The text value is formatted as JSON. Do not parse the JSON. Just put each JSON response in the list.

5. Display each list item in the console.