# Inventory and Sales Management System

This is a simple Python-based console application designed to manage an inventory of products, handle sales, and generate various reports for business analysis. The system allows users to interact with a menu to add, update, delete products, register sales, and generate reports about inventory and sales.

## Features

- **Inventory Management**: Add, update, delete, and search for products.
- **Sales Management**: Register sales, calculate total price with optional discount, and update inventory stock.
- **Reports**: 
  - View sales report showing details of every sale.
  - View the top 3 best-selling products based on quantity sold.
  
## System Requirements

- Python 3.x or higher.

## Installation

1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the directory containing the Python file.
3. Run the script using the following command:

   ```bash
   python gestion_inventario.py

Code Explanation
Data Structures

# DEFAULT_DISCOUNT 
It is used as the default value for the discount, and if the user does not provide a value in the input (i.e., if the discount argument is not passed), the value of DEFAULT_DISCOUNT, which is 0%, will be taken.

 ## Inventory:
The inventory is a list of dictionaries where each dictionary represents a product in the system. Each product contains the following attributes:

 **title**: The title of the product (e.g., book title).

 **price**: The price of the product.

 **stock**: The quantity of the product available in inventory.

 **category**: The category of the product (e.g., Fiction, Adventure).

**author**: The author or creator of the product (relevant for books).

Example:

## inventory = [
    {"title": "El amor en los tiempos del cólera", "price": 1500.00, "stock": 5, "category": "Fiction", "author": "Gabriel García Márquez"},
    {"title": "1984", "price": 800.00, "stock": 8, "category": "Dystopian", "author": "George Orwell"},
    # More products...
]


## Sales:
The sales is a list that stores details about each sale transaction. Each sale includes:

 1. client_name: The name of the client.

 2. title: The title of the product sold.

 3. quantity: The quantity of the product sold.

 4. total_price: The total price of the sale, possibly after applying a discount.

 5. date: The timestamp when the sale was made.
 
 Example: 
 # sales = []

 ## Functions and Core Logic
1. Show Menu (show_menu)

Displays the main menu of the application, allowing the user to select different operations such as adding a product, viewing the inventory, registering a sale, etc.

2. Add Product (add_product)

This function allows the user to add a new product to the inventory. The product details include title, author, category, price, and stock.

3. Show Inventory (show_inventory)

This function displays all the products in the inventory with their details: title, author, category, price, and stock.

4. Search Product (search_product)

This function allows the user to search for a product in the inventory by its title.

5. Delete Product (delete_product)

This function allows the user to delete a product from the inventory based on its title.

6. Update Product (update_product)

This function allows the user to update the details of an existing product (title, author, category, price, stock).

7. Register Sale (register_sale)

This function handles the sale of a product. The sale includes client name, product title, quantity, and optional discount. If the sale is successful, the product stock is updated.

8. Sales Report (show_sales_report)

This function displays a report of all registered sales, showing client name, product title, quantity sold, total price, and the date of the sale.

9. Top 3 Best-Selling Products (show_top_selling_products)

This function calculates the top 3 best-selling products based on quantity sold.

## Main Program Flow

The main function contains the interactive loop that presents the menu to the user and processes their input accordingly. Depending on the choice, it calls the appropriate function for product management, sales registration, or report generation.