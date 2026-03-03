## Test Case: Verify Progress Bar Functionality

### Test Steps

1. Open the main page of the website
2. Click on **Widgets**
3. Click on **Progress Bar**
4. Verify Progress Bar starts at 0%
5. Click on **Start**
6. Verify Progress Bar starts, progress should increase from 0%
7. Verify Progress Bar completes successfully, progress should be at 100%, button should say **Reset**

---

### Key Attributes

1. **Title**  
   Verify Progress Bar Functionality

2. **Objective**  
   Ensure that the Progress Bar starts, runs and completes successfully.

3. **Preconditions**  
   - Pytest and Playwright are installed  

4. **Test Environment**  
   - Programming Language: Python  
   - Browser: Google Chrome  
   - Test Framework: Pytest with Playwright

5. **Navigation Steps**  
   Open homepage → Widgets → Progress Bar

6. **Test Steps / Actions**  
   - Open the Progress Bar page
   - Start progress bar  
   - Verify progress bar starts
   - Wait for progress bar to complete 
   - Verify progress bar completes

7. **Expected Results**  
   - Progress Bar successfully starts
   - Progress Bar successfully runs
   - Progress Bar successfully completes

10. **Postconditions**  
    - Progress Bar is at 100%