import time

class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product(ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Category: {self.category})"

def load_product_data(file_path):
    products = []
    with open(file_path, 'r') as file:
        for line in file:
            product_id, name, price, category = line.strip().split(', ')
            products.append(Product(product_id, name, float(price), category))
    return products

def insert_product(products, product):
    products.append(product)
    print(f"Inserted product: {product}")

def update_product(products, product_id, name=None, price=None, category=None):
    for product in products:
        if product.product_id == product_id:
            if name is not None:
                product.name = name
            if price is not None:
                product.price = price
            if category is not None:
                product.category = category
            print(f"Updated product ID {product_id}: {product}")
            return

def delete_product(products, product_id):
    product_name = next((product.name for product in products if product.product_id == product_id), None)
    products[:] = [product for product in products if product.product_id != product_id]
    if product_name:
        print(f"Deleted product ID {product_id}: {product_name}")

def search_product(products, key, value):
    results = [product for product in products if getattr(product, key) == value]
    for product in results:
        print(f"Found product: {product}")
    return results

def bubble_sort(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n-i-1):
            if products[j].price > products[j+1].price:
                products[j], products[j+1] = products[j+1], products[j]

def insertion_sort(products):
    for i in range(1, len(products)):
        key = products[i]
        j = i - 1
        while j >= 0 and key.price < products[j].price:
            products[j + 1] = products[j]
            j -= 1
        products[j + 1] = key

def time_sorting_algorithm(sort_func, products):
    start_time = time.time()
    sort_func(products)
    end_time = time.time()
    return end_time - start_time

def main():
    products = load_product_data('product_data.txt')

    # Perform operations as per the assignment requirements

    # Insert a new product (example)
    new_product = Product('99501', 'Test Product', 99.99, 'Test Category')
    insert_product(products, new_product)

    # Update an existing product
    update_product(products, '40374', price=950.00)

    # Delete a product
    delete_product(products, '34863')

    # Search for a product by name
    search_results = search_product(products, 'name', 'Camera SBBHC')
    print(f"Search Results: {[p.name for p in search_results]}")

    # Sort products
    bubble_sort(products)
    print("Products sorted by Bubble Sort:")
    for p in products:
        print(f"{p.name}: {p.price}")

    # Measure and compare sorting times
    print("Measuring sorting times...")
    time_bubble_sorted = time_sorting_algorithm(bubble_sort, products[:])
    time_bubble_reverse = time_sorting_algorithm(bubble_sort, list(reversed(products)))
    time_insertion_sorted = time_sorting_algorithm(insertion_sort, products[:])
    time_insertion_reverse = time_sorting_algorithm(insertion_sort, list(reversed(products)))

    print(f"Bubble Sort (sorted): {time_bubble_sorted:.10f} seconds")
    print(f"Bubble Sort (reverse): {time_bubble_reverse:.10f} seconds")
    print(f"Insertion Sort (sorted): {time_insertion_sorted:.10f} seconds")
    print(f"Insertion Sort (reverse): {time_insertion_reverse:.10f} seconds")

if __name__ == "__main__":
    main()
