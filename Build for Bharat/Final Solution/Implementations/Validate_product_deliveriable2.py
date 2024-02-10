import qrcode
import os
import pandas as pd

# List of valid prefixes
valid_prefixes = ['123', '301', '302', '303', '304', '305', '308', '309', '310']

# Function to generate QR code for a given product ID and order ID and save it
def generate_and_save_qr_code(product_id, is_valid, output_directory):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
<<<<<<< HEAD
    qr_data = f"Product ID : {product_id}, Product Status : {'Valid' if is_valid else 'Invalid'}"
=======
    qr_data = f"Product ID: {product_id}, Product Status : {'Valid' if is_valid else 'Invalid'}"
>>>>>>> bd5c51aed221a3a16c3be038ac0e0437cd7130cc
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    file_path = os.path.join(output_directory, f"{product_id}.png")
    qr.make_image(fill_color="black", back_color="white").save(file_path)
    return file_path

# Function to generate QR codes for a list of product IDs and save them
def generate_qr_codes(product_ids, output_directory):
    qr_mapping = {}
    for product_id in product_ids:
        try:
            # Check if product_id is a string
            if not isinstance(product_id, str):
                print(f"Skipping non-string value: {product_id}")
                continue
            
            # Check if product_id starts with valid prefix
            is_valid = any(product_id.startswith(prefix) for prefix in valid_prefixes)
            file_path = generate_and_save_qr_code(product_id, is_valid, output_directory)
            qr_mapping[product_id] = file_path
        except Exception as e:
            print(f"Error processing product ID '{product_id}': {e}")
    
    return qr_mapping

#df = pd.DataFrame({'PRODUCT ID': ['1234679.0', '1234657.0', '1234701.0', '1234613.0', '1234789.0']})

