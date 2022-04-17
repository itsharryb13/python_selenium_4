
from behave import given, then
from selenium.webdriver.common.by import By



color_option = (By.CSS_SELECTOR, "#variation_color_name li")
selected_color = (By.CSS_SELECTOR, "#variation_color_name span.selection")


@given('Open Amazon {productid} page')
def open_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/')

@then('Verify select through colors')
def verify_dress_color(context):
    colors = context.driver.find_elements(*color_option)
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage', 'Light Wash',
                       'Medium Vintage','Medium Wash', 'Rinse', 'Rinsed Vintage', 'Vintage Light Wash', 'Washed Black']

    for i in range(len(colors)):
        colors[i].click()
        color_text = context.driver.find_element(*selected_color).text
        assert color_text == expected_colors[i], f"Color don't match. Expected {expected_colors[i]} but got {color_text}"

    print("Test Passed")
    context.driver.quit()








