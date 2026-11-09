def test_inspect_login_elements(page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")

    inputs = page.locator("input").evaluate_all("""
        elements => elements.map(el => ({
            type: el.type,
            name: el.name,
            placeholder: el.placeholder,
            id: el.id
        }))
    """)

    buttons = page.locator("button").evaluate_all("""
        elements => elements.map(el => ({
            text: el.innerText,
            type: el.type
        }))
    """)

    print("INPUT FIELDS:", inputs)
    print("BUTTONS:", buttons)
