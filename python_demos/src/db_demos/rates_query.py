""" rates query demo """

import pyodbc

conn_options = [
    "DRIVER={ODBC Driver 17 for SQL Server}",
    "SERVER=localhost,1433",
    "DATABASE=ratesapp",
    "UID=sa",
    "PWD=sqlDbp@ss!"
]


conn_string = ";".join(conn_options)

# print(conn_string)

def main() -> None:
    """ main """

    with pyodbc.connect(conn_string) as con:

        rates = con.execute("select currencysymbol as symbol from rates")

        for rate in rates:
            # print(rate[2])
            print(rate)
            # print(rate.CurrencySymbol)
            # print(rate.currencysymbol)
            print(rate.symbol)
            # print(rate["CurrencySymbol"])
            # print(rate.__dict__)

        print("get one rate")

        rate_id = 1

        rates = con.execute(
            "select currencysymbol as symbol from rates where ratesid = ?", (rate_id,))


        for rate in rates:
            print(rate)

if __name__ == "__main__":
    main()
