## Test Case: Verify Dynamic Properties

### Test Steps

1. Open the main page of the website
2. Click on **Elements**
3. Verify that disabled **Will enable 5 seconds** button enables after 5 seconds (with slight buffer)
4. Verify that invisible **Visible After 5 Seconds** button turns visible after 5 seconds (with slight buffer)

---

### Key Attributes

1. **Title**  
   Verify Dynamic Properties

2. **Objective**  
   Ensure Dynamic Properties are detected

3. **Preconditions**  
   - Pytest and Playwright are installed  

4. **Test Environment**  
   - Programming Language: Python  
   - Browser: Google Chrome  
   - Test Framework: Pytest with Playwright

5. **Navigation Steps**  
   Open homepage → Elements → Dynamic Properties

6. **Test Steps / Actions**  
   - Open the Dynamic Properties page
   - Wait until buttons change
   - Verify buttons changed

7. **Expected Results**  
   - Button enables after 5 seconds
   - Button turns visible after 5 seconds

10. **Postconditions**  
    - Button enables after 5 seconds
    - Button turns visible after 5 seconds