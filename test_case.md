## Test Case: Verify Shopping Cart CRUD Functionality

### Test Steps

1. Open the main page of the application.
2. Click on the **Computers** category.
3. Click on the **Desktops** subcategory.
4. Add the **first listed computer** to the shopping cart using the **default configuration**.
5. Click on **Shopping Cart**.
6. Verify that the selected computer is displayed in the shopping cart.
7. Click **Edit** for the computer in the shopping cart.
8. Select **Processor = Fast**.
9. Select **RAM = 4 GB**.
10. Select **HDD = 400 GB**.
11. Select the **Image Viewer** option.
12. Click **Update**.
13. Click on **Shopping Cart**.
14. Verify that the **updated specifications and price** are displayed correctly.
15. Select the **Remove** checkbox for the product.
16. Click **Update Shopping Cart**.
17. Verify that the product is removed from the shopping cart.
18. Navigate to **Computers → Desktops**.
19. Add **all computers with a price greater than $800** to the shopping cart using the **default configuration**.
20. Open the **Shopping Cart**.
21. Verify that **all selected computers** are displayed in the shopping cart.
22. Select **all products** in the shopping cart.
23. Click **Remove / Update Shopping Cart**.
24. Verify that the shopping cart is **empty**.

---

### Key Attributes

1. **Title**  
   Verify Shopping Cart CRUD Functionality

2. **Objective**  
   Ensure that shopping cart functionality works correctly, including adding products, updating product configurations, verifying price changes, and removing products.

3. **Preconditions**  
   - Pytest and Playwright are installed  
   - User has access to the Demo Web Shop homepage  
   - Shopping cart is initially empty

4. **Test Environment**  
   - Programming Language: Python  
   - Browser: Google Chrome  
   - Test Framework: Pytest with Playwright

5. **Test Data**  
   - Desktop product: *Build your own cheap computer*  
   - Updated configuration options:  
     - Processor = Fast  
     - RAM = 4 GB  
     - HDD = 400 GB  
     - Image Viewer selected
    - Desktop products with price greater than **$800**
    - The first available specification option is selected

6. **Navigation Steps**  
   Open homepage → Computers → Desktops → Product page → Shopping Cart

7. **Test Steps / Actions**  
   - Add a computer to the shopping cart  
   - Verify shopping cart contents  
   - Edit and update product configuration  
   - Re-verify updated specifications and price  
   - Add multiple products with price greater than $800  
   - Remove all products from the shopping cart

8. **Expected Results**  
   - Added products appear in the Shopping Cart  
   - Updated product specifications and total price are displayed correctly  
   - Products are successfully removed from the cart when selected  

9. **Priority & Severity**  
   - Priority: High  
   - Severity: Critical

10. **Postconditions**  
    - Shopping cart is empty