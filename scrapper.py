from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import random

# Set up Selenium WebDriver
chrome_driver_path = "<Insert Chrome Driver Path>"
service = Service(chrome_driver_path)

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run headless for faster scraping
options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid bot detection
driver = webdriver.Chrome(service=service, options=options)

# n8n AI workflows page
n8n_url = "https://n8n.io/workflows/categories/ai/"
driver.get(n8n_url)

# Wait for workflow elements to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a.templateLink_NQWU6"))
)

# Click "Load more templates" button until no more are available
while True:
    try:
        load_more_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.load-more-link"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", load_more_button)
        time.sleep(2)  # Wait for scroll to complete
        load_more_button.click()
        time.sleep(3)  # Wait for new templates to load
        print("Loaded more templates...")
    except Exception as e:
        print("No more templates to load")
        break

# Now get all workflow elements after loading everything
workflow_elements = driver.find_elements(By.CSS_SELECTOR, "a.templateLink_NQWU6")
workflows = []

for workflow in workflow_elements:
    # Check if the workflow is free
    try:
        status_element = workflow.find_element(By.CSS_SELECTOR, "div.paidOrFree_jrepT")
        status = status_element.text.strip().lower()
        
        if status != "free":
            continue  # Skip if not free
            
        title = workflow.text.strip()
        link = workflow.get_attribute("href")

        if not link.startswith("http"):  # Ensure proper URL
            link = "https://n8n.io/workflows" + link

        workflows.append({"title": title, "url": link})
        print(f"Found free workflow: {title}")
        
    except Exception as e:
        print(f"Failed to check workflow status: {e}")

print(f"Found {len(workflows)} free workflows!")

# Visit each workflow page and extract workflow JSON
workflow_data = []

for workflow in workflows:
    driver.get(workflow["url"])
    time.sleep(random.uniform(2, 5))  # Allow page to load

    try:
        # Extract JSON from <n8n-demo workflow="...">
        workflow_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "n8n-demo"))
        )

        workflow_json = workflow_element.get_attribute("workflow")

        if not workflow_json:
            workflow_json = "No JSON found"

        workflow_data.append({
            "title": workflow["title"],
            "url": workflow["url"],
            "json": workflow_json
        })

        print(f"Extracted: {workflow['title']}")

    except Exception as e:
        print(f"Failed to extract: {workflow['title']} - {e}")

# Close the driver
driver.quit()

# Save data to JSON file
with open("n8n_ai_workflows.json", "w", encoding="utf-8") as f:
    json.dump(workflow_data, f, indent=4)

print("Scraping complete! Data saved to n8n_ai_workflows.json")
