CREATE USER student WITH PASSWORD 'password';
GRANT CONNECT ON DATABASE technique TO student;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO student;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO student;


-- Создание таблицы "Продукты"
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Category VARCHAR(50) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL
);

-- Создание таблицы "Поставщики"
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY,
    Company VARCHAR(100),
    Phone VARCHAR(20)
);

-- Создание таблицы "Клиенты"
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Phone VARCHAR(20)
);

-- Создание таблицы "Заказы"
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Создание таблицы "СоставЗаказа"
CREATE TABLE OrderDetails (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);