cookies_kg_price_str = "860"

cookies_kg_price_int = int(cookies_kg_price_str)  # цена за кг печенья
friends_counts = 5 # количество друзей

personal_fee = round(cookies_kg_price_int / friends_counts)

print(f"Дорогой друг! Надеюсь, печенье понравилось, верни, пожалуйста, {personal_fee}!")