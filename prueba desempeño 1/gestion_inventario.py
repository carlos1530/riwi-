import datetime

#Constants 
DEFAULT_DISCOUNT = 0 #Default discount if none is provided 

# Initialize the inventory with a few sample products
# Each product is a dictionary containing: title, price, stock, category, and author
inventory = [
    { "title": "El amor en los tiempos del cólera", "price": 1500.00, "stock": 5, "category": "Fiction", "author": "Gabriel García Márquez" },
    { "title": "Cien años de soledad", "price": 1200.00, "stock": 10, "category": "Fiction", "author": "Gabriel García Márquez" },
    { "title": "1984", "price": 800.00, "stock": 8, "category": "Dystopian", "author": "George Orwell" },
    { "title": "El gran Gatsby", "price": 900.00, "stock": 6, "category": "Fiction", "author": "F. Scott Fitzgerald" },
    { "title": "moby-dick", "price": 1100.00, "stock": 4, "category": "Adventure", "author": "Herman Melville" },
]
# List to store details of sales made (each sale is represented as a dictionary)
sales = []
#function to display the main menu of options for the user
def show_menu():
    print("\n--- Inventory and Sales Management ---")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Search product")
    print("4. Delete product")
    print("5. Update product")
    print("6. Register sale")
    print("7. show income report")
    print("8. Show sales report")
    print("9. Show top selling products")
    print("10. show sales by author")
    print("9. Exit")
#funtion to add a new product to the inventory
# It takes the product's title, author, category, price, and stock as arguments.
def add_product(title, author, category, price, stock):
    if price < 0 or stock < 0:
        print("Price and stock must be positive numbers.")
        return
    #create a dictionary for th new product
    product = {"title": title, "author": author, "category": category, "price": price, "stock": stock}
    #Add the product to the inventory list
    inventory.append(product)
    #confirm that the product was added successfully
    print(f"Product '{title}' added successfully!")
# Function to display the current inventory 
# If inventory is empty, display a message 
def show_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    #Loop throught the inventory and print details of each product
    print("\nInventory:")
    for i, product in enumerate(inventory, 1):
        print(f"{i}. Title: {product['title']} | Author: {product['author']} | Category: {product['category']} "
              f"| Price: ${product['price']:.2f} | Stock: {product['stock']}")
# Function to search for a product by title
# It returns the product if found, otherwise returns None.
def search_product(title):
    for product in inventory:
        if product['title'].lower() == title.lower():
            return product
    return None
# Function to delete a product from the inventory 
# If the product is found it is removed from the inventory 
def delete_product(title):
    product = search_product(title)
    if product:
        inventory.remove(product)
        print(f"Product '{title}' deleted.")
    else:
        # If the product was not found, display an error message
        print("Product not found.")

#funtction to update an existing product's details
#It alllows updating the title, author, category, price, and stock of a product
def update_product(title):
    product = search_product(title)
    if product:
        print(f"Product found: {product}")
        # Ask the user for new details, allowing them to keep current values by pressing Enter
        new_title = input("Enter new title (or press Enter to keep current): ") or product['title']
        new_author = input("Enter new author (or press Enter to keep current): ") or product['author']
        new_category = input("Enter new category (or press Enter to keep current): ") or product['category']
        new_price = input("Enter new price (or press Enter to keep current): ")
        new_stock = input("Enter new stock (or press Enter to keep current): ")
        # validate and process the new price and stock inputs
        if new_price:
            new_price = float(new_price)
            if new_price < 0:
                print("Price must be a positive number.")
                return
        else:
            new_price = product['price']
        
        if new_stock:
            new_stock = int(new_stock)
            if new_stock < 0:
                print("Stock must be a non-negative integer.")
                return
        else:
            new_stock = product['stock']
        # Update the product dictionary with new values
        product.update({
            'title': new_title,
            'author': new_author,
            'category': new_category,
            'price': new_price,
            'stock': new_stock
        })
        print(f"Product '{title}' updated successfully!")
    else:
        print("Product not found.")

# Function to register a sale transaction
# It reduces the stock of the product sold and records the sale details to the sales list
def register_sale(client_name, title, quantity, discount=DEFAULT_DISCOUNT):
    product = search_product(title)
    if product:
        # check if there is enough stock for the sale
        if product["stock"] < quantity:
            print("Insufficient stock for this product.")
            return
        # Calculate the total price after applying the discount
        total_price = product["price"] * quantity * (1 - discount / 100)
        # Create a sale dictionary with details of the transaction
        sale = {
            "client_name": client_name,
            "title": title,
            "quantity": quantity,
            "total_price": total_price,
            "date": datetime.datetime.now()
        }
        # Append the sale to the sales list 
        sales.append(sale)
        # Update the stock of the product sold 
        product["stock"] -= quantity
        print(f"Sale registered: {sale}")
    else:
        print("Product not found.")


# Function to show the total gross and net incom
def show_income_report():
    total_gross = 0
    total_net = 0
    for sale in sales:
        total_gross += sale['total_price'] / (1 - sale['discount'] / 100)
        total_net += sale['total_price']
    print(f"Total Gross Income (before discounts): ${total_gross:.2f}")
    print(f"Total Net Income (after discounts): ${total_net:.2f}")

# Function to display a sales report
# It lists all sales with details like client name, product, quantity and total price
def show_sales_report():
    if not sales:
        print("No sales registered.")
        return
    print("\nSales Report:")
    for sale in sales:
        print(f"Client: {sale['client_name']} | Product: {sale['title']} | Quantity: {sale['quantity']} "
              f"| Total Price: ${sale['total_price']:.2f} | Date: {sale['date']}")

# Function to show the top 3 best-selling products based on quantity sold        
def show_top_selling_products():
    if not sales:
        print("No sales registered.")
        return
    product_sales = {}
    # Count the total quantity sold per product 
    for sale in sales:
        title = sale['title']
        if title in product_sales:
            product_sales[title] += sale['quantity']
        else:
            product_sales[title] = sale['quantity']

    # Sort products by quantity sold in descending order and take the top 3 
    sorted_sales = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
    top_selling = sorted_sales[:3]
    
    print("\nTop 3 Best-Selling Products:")
    for title, quantity in top_selling:
        print(f"Product: {title} | Quantity Sold: {quantity}")

# Function to show the sales grouped by author
def show_sales_by_author():
    if not sales:
        print("No sales registered.")
        return
    author_sales = {}
    for sale in sales:
        product = search_product(sale['title'])
        author = product['author']
        if author in author_sales:
            author_sales[author] += sale['total_price']
        else:
            author_sales[author] = sale['total_price']
    print("\nSales by Author:")
    for author, total in author_sales.items():
        print(f"Author: {author} | Total Sales: ${total:.2f}")


# Main function to handle the overall program flow 
def main():     
    continuar= True  # Continue the loop until the user chooses to exzit 
    while continuar:
        #Show the main menu 
        show_menu()
        # Take user imput for selecting an option 
        choice = input("Select an option (1-9): ")
        # Handle each option acording to the user's choice 
        if choice == '1':
            title = input("Enter product title: ")
            author = input("Enter author: ")
            category = input("Enter category: ")
            price = float(input("Enter price: "))
            stock = int(input("Enter stock: "))
            add_product(title, author, category, price, stock)
        elif choice == '2':
            show_inventory()
        elif choice == '3':
            title = input("Enter product title to search: ")
            product = search_product(title)
            if product:
                print(f"Product found: {product}")
            else:
                print("Product not found.")
        elif choice == '4':
            title = input("Enter product title to delete: ")
            delete_product(title)
        elif choice == '5':
            title = input("Enter product title to update: ")
            update_product(title)
        elif choice == '6':
            client_name = input("Enter client name: ")
            title = input("Enter product title for sale: ")
            quantity = int(input("Enter quantity sold: "))
            discount = float(input("Enter discount percentage (default 0): ") or 0)
            register_sale(client_name, title, quantity, discount)
        elif choice == '7':
            show_income_report()
        elif choice == '8':
            show_sales_report()
        elif choice == '9':
            show_top_selling_products()
        elif choice == '10':
            show_sales_by_author()
        elif choice == '11':
            print("Exiting the program.")
            continuar= False # Exit the loop and end the program 
        else:
            print("Invalid option. Please try again.")

# Ensure the program runs only when this script is executed directly
if __name__ == "__main__":
    main()