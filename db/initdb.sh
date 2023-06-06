#! /bin/bash

table1="products"
table2="suppliers"
table3="Customers"
table4="Orders"
table5="OrderDetails"



for i in {1..5}; do
    #TABLE1
    product_title=$(shuf -n 1 datasets/products/products.txt)
    category=$(shuf -n 1 datasets/products/product_category.txt)
    psql -U root -d technique -c "INSERT INTO $table1 (ProductID, Title, Category, Price) values ($i, '$product_title', '$category', $RANDOM);"
    
    #TABLE2
    company_title=$(shuf -n 1 datasets/suppliers/company.txt)
    company_phone=$(( ( RANDOM % 89259999999 )  + 89250000000 ))
    psql -U root -d technique -c "INSERT INTO $table2 (SupplierID, Company, Phone) values ($i, '$company_title', $company_phone);"
    
    #TABLE3
    name=$(shuf -n 1 datasets/customers/names.txt)
    lastname=$(shuf -n 1 datasets/customers/lastnames.txt)
    customers_phone=$(( ( RANDOM % 89259999999 )  + 89250000000 ))
    psql -U root -d technique -c "INSERT INTO $table3 (CustomerID, FirstName, LastName, Phone) values ($i, '$name', '$lastname', $customers_phone);"
    
done

for i in {1..5}; do
    #TABLE4
    customerID=$(( ( RANDOM % 5 )  + 1 ))
    date=$(shuf -n1 -i$(date -d '2020-01-01' '+%s')-$(date -d '2023-01-01' '+%s') | xargs -I{} date -d '@{}' '+%Y-%m-%d')
    psql -U root -d technique -c "INSERT INTO $table4 (OrderID, CustomerID, OrderDate) values ($i, '$customerID', '$date');"
    
    #TABLE5
    productID=$(( ( RANDOM % 5 )  + 1 ))
    quantity=$(( ( RANDOM % 700 )  + 20 ))
    psql -U root -d technique -c "INSERT INTO $table5 (OrderID, ProductID, Quantity) values ($i, '$productID', '$quantity');"
done