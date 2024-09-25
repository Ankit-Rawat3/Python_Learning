from fpdf import FPDF

# Data for the PDF
content = {
    "Challenges in Automation Testing": [
        "1. Handling Dynamic Web Elements",
        "2. Browser Compatibility Issues",
        "3. Synchronization between Test Cases and Web Elements",
        "4. Managing Test Data",
        "5. Maintaining Test Scripts for Large Applications",
        "6. Parallel Execution of Tests",
        "7. Integration with CI/CD pipelines",
        "8. Scaling Automation with Cloud Services (e.g., Selenium Grid)",
    ],
    "Common Errors": [
        "1. Element Not Found (NoSuchElementException)",
        "2. TimeoutException (Element Not Interactable)",
        "3. StaleElementReferenceException",
        "4. WebDriver Initialization Issues",
        "5. Incorrect XPath/CSS Selectors",
        "6. Test Data Not Loading Properly",
        "7. Incorrect Browser Driver Configuration",
    ],
    "Interview Questions for Automation Testing": [
        "1. What is Selenium WebDriver and how does it work?",
        "2. Explain the Page Object Model (POM).",
        "3. How do you handle dynamic elements in Selenium?",
        "4. What are waits in Selenium and why are they important?",
        "5. How can you execute tests in parallel?",
        "6. What are the advantages of automation testing over manual testing?",
        "7. How do you integrate Selenium with CI/CD tools like Jenkins?",
        "8. Explain the use of TestNG/PyTest in automation testing.",
    ],
    "Common Exceptions in Selenium": [
        "1. NoSuchElementException: Element could not be found.",
        "2. StaleElementReferenceException: The element is no longer present on the DOM.",
        "3. TimeoutException: The command did not complete within the given time.",
        "4. ElementNotVisibleException: The element is not visible for interaction.",
        "5. WebDriverException: General WebDriver error.",
        "6. InvalidSelectorException: Invalid XPath or CSS selector.",
    ],
}

# Initialize PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Automation Testing Challenges, Errors, Interview Questions, and Exceptions", ln=True, align="C")
pdf.ln(10)

# Content section by section
pdf.set_font("Arial", size=12)

for section, items in content.items():
    # Section title
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt=section, ln=True)
    pdf.ln(5)

    # Section content
    pdf.set_font("Arial", size=12)
    for item in items:
        pdf.cell(200, 10, txt=item, ln=True)
    pdf.ln(5)

# Save the PDF
pdf_file_path = "D:/Ankit Essentials/automation_testing_challenges.pdf"
pdf.output(pdf_file_path)

pdf_file_path
