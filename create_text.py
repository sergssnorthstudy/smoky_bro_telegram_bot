

def create_view_categories(categories:list) -> str:
    finish_string = ""
    for catergory in categories:
        catergory_id = catergory[0]
        catergory_name = catergory[1]
        finish_string += f"{catergory_id}. {catergory_name}\n"
    return finish_string


def create_view_brands(brands:list) -> str:
    finish_string = ""
    for brand in brands:
        brand_id = brand[0]
        brand_name = brand[1]
        finish_string += f"{brand_id}. {brand_name}\n"
    return finish_string
