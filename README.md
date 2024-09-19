
                             Convenience Store
1. Single Responsibility Principle (SRP): Each class has a single responsibility: * Product class is responsible for representing a product with its attributes (name, price, quantity). * ConvenienceStore class is responsible for managing the inventory of products.

2. Separation of Concerns (SoC): Each class is concerned with its own specific functionality: * Product class is concerned with product-related attributes and behavior. * ConvenienceStore class is concerned with store-related functionality (adding, removing, displaying products).

3. Encapsulation: Each class encapsulates its data and behavior: * Product class encapsulates its attributes (name, price, quantity) and provides a __str__ method to format its output. * ConvenienceStore class encapsulates its list of products and provides methods to add, remove, and display products.

4. Abstraction: The code abstracts away the implementation details: * The Product class abstracts away the details of how a product is represented. * The ConvenienceStore class abstracts away the details of how the inventory is managed.

5. Composition: The ConvenienceStore class is composed of a list of Product objects: * This allows the store to manage multiple products without having to know the details of each product.

6. Interface Segregation Principle (ISP): The ConvenienceStore class provides a simple interface for adding, removing, and displaying products: * This makes it easy to use and extend the class without having to know the implementation details.

7. Don't Repeat Yourself (DRY): The code avoids duplication: * The Product class is reused in the ConvenienceStore class to represent each product in the inventory.

8. KISS (Keep it Simple, Stupid): The code is simple and easy to understand: * Each class has a clear and concise implementation. * The code uses simple and intuitive method names.
