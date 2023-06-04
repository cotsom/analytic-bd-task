-- Создание таблицы "Продукты"
CREATE TABLE Products (
    `ProductID` INT PRIMARY KEY,
    `Name` VARCHAR(100) NOT NULL,
    `Category` VARCHAR(50) NOT NULL,
    `Price` DECIMAL(10, 2) NOT NULL
);

-- Создание таблицы "Поставщики"
CREATE TABLE Suppliers (
    `SupplierID` INT PRIMARY KEY,
    `Name` VARCHAR(100) NOT NULL,
    `ContactPerson` VARCHAR(100),
    `Phone` VARCHAR(20),
    `Email` VARCHAR(100)
);

-- Создание таблицы "Клиенты"
CREATE TABLE Customers (
    `CustomerID` INT PRIMARY KEY,
    `FirstName` VARCHAR(50) NOT NULL,
    `LastName` VARCHAR(50) NOT NULL,
    `Address` VARCHAR(100),
    `Phone` VARCHAR(20),
    `Email` VARCHAR(100)
);

-- Создание таблицы "Заказы"
CREATE TABLE Orders (
    `OrderID` INT PRIMARY KEY,
    `CustomerID` INT,
    `OrderDate` DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Создание таблицы "СоставЗаказа"
CREATE TABLE OrderDetails (
    `OrderID` INT,
    `ProductID` INT,
    `Quantity` INT,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);