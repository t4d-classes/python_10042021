""" connection demo """

import pyodbc

conn_options = [
    "DRIVER={ODBC Driver 17 for SQL Server}",
    "SERVER=localhost,1433",
    "DATABASE=ratesapp",
    "UID=sa",
    "PWD=sqlDbp@ss!"
]


conn_string = ";".join(conn_options)

print(conn_string)

def main() -> None:
    """ main """

    with pyodbc.connect(conn_string) as con:

        rates = con.execute("select * from rates")

        for rate in rates:
            print(rate)

if __name__ == "__main__":
    main()
